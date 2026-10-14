using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.Rendering;

public class PythonReceiver : MonoBehaviour
{
    private const string HOST = "127.0.0.1";
    private const int PORT = 5000;

    [SerializeField]
    private MeshFilter meshFilter;

    [SerializeField]
    private float Spacing = 0.01f;


    // --------------------------------------------------
    // Grid setup
    // --------------------------------------------------

    private int GRID_ROWS;
    private int GRID_COLS;

    private int TotalPoints;
    private int FrameSize;

    private float HEIGHT_MULTIPLIER;


    // --------------------------------------------------
    // Network
    // --------------------------------------------------

    private TcpClient client;
    private NetworkStream stream;


    // --------------------------------------------------
    // Mesh
    // --------------------------------------------------

    private Mesh mesh;

    private Vector3[] vertices;
    private int[] triangles;


    // --------------------------------------------------
    // Frame data
    // --------------------------------------------------

    private byte[] frameBuffer;

    private float[] latestHeights;
    private float[] renderHeights;

    private readonly object frameLock = new object();

    private bool hasNewFrame;


    // --------------------------------------------------
    // Setup message
    // --------------------------------------------------

    [Serializable]
    private class SetupMessage
    {
        public string type;
        public int GRID_ROWS;
        public int GRID_COLS;
        public float HEIGHT_MULTIPLIER;
    }


    // --------------------------------------------------
    // Start
    // --------------------------------------------------

    private async void Start()
    {
        try
        {
            client = new TcpClient();

            await client.ConnectAsync(
                HOST,
                PORT
            );

            stream = client.GetStream();

            Debug.Log("Connected to Python.");


            // Receive grid dimensions before creating the mesh
            await ReceiveSetup();


            // Create the mesh using Python dimensions
            InitializeMesh();


            // Start binary frame receiver on a worker thread
            _ = Task.Run(ReceiveData);
        }
        catch (Exception exception)
        {
            Debug.LogError(
                $"Python connection error: {exception}"
            );
        }
    }


    // --------------------------------------------------
    // Receive setup
    // --------------------------------------------------

    private async Task ReceiveSetup()
    {
        // First 4 bytes contain the JSON message size
        byte[] lengthBuffer = new byte[4];

        await ReadExactAsync(
            lengthBuffer,
            lengthBuffer.Length
        );


        // Python sends the integer as little-endian
        int jsonLength =
            lengthBuffer[0] |
            (lengthBuffer[1] << 8) |
            (lengthBuffer[2] << 16) |
            (lengthBuffer[3] << 24);


        if (jsonLength <= 0)
        {
            throw new IOException(
                $"Invalid setup message length: {jsonLength}"
            );
        }


        // Read the setup JSON
        byte[] jsonBuffer = new byte[jsonLength];

        await ReadExactAsync(
            jsonBuffer,
            jsonLength
        );


        string json = Encoding.UTF8.GetString(
            jsonBuffer
        );


        SetupMessage setup =
            JsonUtility.FromJson<SetupMessage>(
                json
            );


        if (setup == null)
        {
            throw new IOException(
                "Could not deserialize setup message."
            );
        }


        if (setup.type != "setup")
        {
            throw new IOException(
                $"Unexpected message type: {setup.type}"
            );
        }


        if (
            setup.GRID_ROWS <= 0 ||
            setup.GRID_COLS <= 0
        )
        {
            throw new IOException(
                "Invalid grid dimensions."
            );
        }


        GRID_ROWS = setup.GRID_ROWS;
        GRID_COLS = setup.GRID_COLS;
        HEIGHT_MULTIPLIER = setup.HEIGHT_MULTIPLIER;


        TotalPoints =
            GRID_ROWS *
            GRID_COLS;


        FrameSize =
            TotalPoints *
            sizeof(float);


        // Allocate buffers only after dimensions are known
        frameBuffer =
            new byte[FrameSize];

        latestHeights =
            new float[TotalPoints];

        renderHeights =
            new float[TotalPoints];


        Debug.Log(
            $"Setup received | " +
            $"Rows: {GRID_ROWS} | " +
            $"Cols: {GRID_COLS} | " +
            $"Points: {TotalPoints} | " +
            $"Frame size: {FrameSize} bytes" +
            $"Height Multiplier: {HEIGHT_MULTIPLIER}"
        );
    }


    // --------------------------------------------------
    // Initialize mesh
    // --------------------------------------------------

    private void InitializeMesh()
    {
        mesh = new Mesh();

        mesh.name = "Python Terrain";

        mesh.indexFormat =
            IndexFormat.UInt32;

        mesh.MarkDynamic();


        vertices =
            new Vector3[TotalPoints];


        // Center the mesh around local (0, 0, 0)
        float halfX =
            (GRID_ROWS - 1) *
            Spacing *
            0.5f;

        float halfZ =
            (GRID_COLS - 1) *
            Spacing *
            0.5f;


        for (
            int i = 0;
            i < GRID_ROWS;
            i++
        )
        {
            for (
                int j = 0;
                j < GRID_COLS;
                j++
            )
            {
                int index =
                    GetVertexIndex(
                        i,
                        j
                    );


                vertices[index] =
                    new Vector3(
                        i * Spacing - halfX,
                        0f,
                        j * Spacing - halfZ
                    );
            }
        }


        // Build triangles
        triangles =
            new int[
                (GRID_ROWS - 1) *
                (GRID_COLS - 1) *
                6
            ];


        int triangleIndex = 0;


        for (
            int i = 0;
            i < GRID_ROWS - 1;
            i++
        )
        {
            for (
                int j = 0;
                j < GRID_COLS - 1;
                j++
            )
            {
                int bottomLeft =
                    GetVertexIndex(
                        i,
                        j
                    );

                int bottomRight =
                    GetVertexIndex(
                        i,
                        j + 1
                    );

                int topLeft =
                    GetVertexIndex(
                        i + 1,
                        j
                    );

                int topRight =
                    GetVertexIndex(
                        i + 1,
                        j + 1
                    );


                triangles[triangleIndex++] =
                    bottomLeft;

                triangles[triangleIndex++] =
                    bottomRight;

                triangles[triangleIndex++] =
                    topLeft;


                triangles[triangleIndex++] =
                    bottomRight;

                triangles[triangleIndex++] =
                    topRight;

                triangles[triangleIndex++] =
                    topLeft;
            }
        }


        mesh.vertices =
            vertices;

        mesh.triangles =
            triangles;


        mesh.RecalculateNormals();
        mesh.RecalculateBounds();


        meshFilter.mesh =
            mesh;


        Debug.Log(
            $"Mesh initialized: " +
            $"{GRID_COLS}x{GRID_ROWS}"
        );
    }


    // --------------------------------------------------
    // Receive binary frames
    // --------------------------------------------------

    private async Task ReceiveData()
    {
        try
        {
            while (true)
            {
                // One full frame must always contain
                // GRID_ROWS * GRID_COLS float32 values
                await ReadExactAsync(
                    frameBuffer,
                    FrameSize
                );


                lock (frameLock)
                {
                    Buffer.BlockCopy(
                        frameBuffer,
                        0,
                        latestHeights,
                        0,
                        FrameSize
                    );

                    hasNewFrame = true;
                }
            }
        }
        catch (IOException)
        {
            Debug.Log(
                "Python connection closed."
            );
        }
        catch (ObjectDisposedException)
        {
        }
        catch (Exception exception)
        {
            Debug.LogError(
                $"Receiver error: {exception}"
            );
        }
    }


    // --------------------------------------------------
    // Update Unity mesh
    // --------------------------------------------------

    private void Update()
    {
        bool newFrameAvailable = false;


        lock (frameLock)
        {
            if (hasNewFrame)
            {
                Buffer.BlockCopy(
                    latestHeights,
                    0,
                    renderHeights,
                    0,
                    FrameSize
                );

                hasNewFrame = false;

                newFrameAvailable = true;
            }
        }


        if (!newFrameAvailable)
        {
            return;
        }


        for (
            int index = 0;
            index < TotalPoints;
            index++
        )
        {
            vertices[index].y =
                renderHeights[index];
        }


        mesh.vertices =
            vertices;

        mesh.RecalculateNormals();
        mesh.RecalculateBounds();
    }


    // --------------------------------------------------
    // TCP helper
    // --------------------------------------------------

    private async Task ReadExactAsync(
        byte[] buffer,
        int size
    )
    {
        int received = 0;


        while (received < size)
        {
            int bytesRead =
                await stream.ReadAsync(
                    buffer,
                    received,
                    size - received
                );


            if (bytesRead == 0)
            {
                throw new IOException(
                    "Python disconnected."
                );
            }


            received += bytesRead;
        }
    }


    // --------------------------------------------------
    // Mesh helper
    // --------------------------------------------------

    private int GetVertexIndex(
        int i,
        int j
    )
    {
        return
            i *
            GRID_COLS +
            j;
    }


    // --------------------------------------------------
    // Cleanup
    // --------------------------------------------------

    private void OnDestroy()
    {
        stream?.Close();
        client?.Close();
    }
}