using System;
using System.IO;
using System.Net.Sockets;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.Rendering;

public class PythonReceiver : MonoBehaviour
{
    private const int GridSize = 512;
    private const int TotalPoints = GridSize * GridSize;

    private const float Spacing = 0.01f;

    // Each height is a 32-bit float = 4 bytes
    private const int FrameSize = TotalPoints * sizeof(float);

    [SerializeField] private MeshFilter meshFilter;

    private TcpClient client;
    private NetworkStream stream;

    private Mesh mesh;

    private Vector3[] vertices;
    private int[] triangles;

    // Raw bytes received from Python
    private readonly byte[] frameBuffer = new byte[FrameSize];

    // Latest complete frame received from Python
    private readonly float[] latestHeights = new float[TotalPoints];

    // Frame currently used by Unity
    private readonly float[] renderHeights = new float[TotalPoints];

    private readonly object frameLock = new object();

    private bool hasNewFrame = false;


    private async void Start()
    {
        InitializeMesh();

        client = new TcpClient();

        await client.ConnectAsync(
            "127.0.0.1",
            5000
        );

        stream = client.GetStream();

        _ = Task.Run(ReceiveData);
    }


    private void InitializeMesh()
    {
        mesh = new Mesh();

        mesh.name = "Python Terrain";

        mesh.indexFormat = IndexFormat.UInt32;
        mesh.MarkDynamic();

        vertices = new Vector3[TotalPoints];

        for (int i = 0; i < GridSize; i++)
        {
            for (int j = 0; j < GridSize; j++)
            {
                int index = GetVertexIndex(i, j);

                vertices[index] = new Vector3(
                    i * Spacing,
                    0f,
                    j * Spacing
                );
            }
        }

        triangles =
            new int[(GridSize - 1) * (GridSize - 1) * 6];

        int triangleIndex = 0;

        for (int i = 0; i < GridSize - 1; i++)
        {
            for (int j = 0; j < GridSize - 1; j++)
            {
                int bottomLeft =
                    GetVertexIndex(i, j);

                int bottomRight =
                    GetVertexIndex(i, j + 1);

                int topLeft =
                    GetVertexIndex(i + 1, j);

                int topRight =
                    GetVertexIndex(i + 1, j + 1);


                triangles[triangleIndex++] = bottomLeft;
                triangles[triangleIndex++] = bottomRight;
                triangles[triangleIndex++] = topLeft;

                triangles[triangleIndex++] = bottomRight;
                triangles[triangleIndex++] = topRight;
                triangles[triangleIndex++] = topLeft;
            }
        }

        mesh.vertices = vertices;
        mesh.triangles = triangles;

        mesh.RecalculateNormals();
        mesh.RecalculateBounds();

        meshFilter.mesh = mesh;
    }


    private async Task ReceiveData()
    {
        try
        {
            while (true)
            {
                int received = 0;

                // TCP is a byte stream, so one ReadAsync call
                // is not guaranteed to return the whole frame.
                while (received < FrameSize)
                {
                    int bytesRead = await stream.ReadAsync(
                        frameBuffer,
                        received,
                        FrameSize - received
                    );

                    if (bytesRead == 0)
                    {
                        return;
                    }

                    received += bytesRead;
                }

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
            // Connection closed
        }
        catch (ObjectDisposedException)
        {
            // Connection closed while stopping the application
        }
    }


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


        // X and Z never change.
        // Only update the height of each vertex.
        for (int index = 0; index < TotalPoints; index++)
        {
            vertices[index].y = renderHeights[index];
        }


        mesh.vertices = vertices;

        mesh.RecalculateNormals();
        mesh.RecalculateBounds();
    }


    private int GetVertexIndex(int i, int j)
    {
        return i * GridSize + j;
    }


    private void OnDestroy()
    {
        stream?.Close();
        client?.Close();
    }
}