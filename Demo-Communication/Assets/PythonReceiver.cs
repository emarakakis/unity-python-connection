using System.IO;
using System.Net.Sockets;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.Rendering;
using System.Diagnostics;

[System.Serializable]
public class PythonData
{
    public int i;
    public int j;
    public float x;
    public float y;
    public float z;
}

[System.Serializable]
public class PythonFrame
{
    public PythonData[] points;
}

public class PythonReceiver : MonoBehaviour
{
    private const int GridSize = 512;

    [SerializeField] private MeshFilter meshFilter;

    private TcpClient client;
    private StreamReader reader;

    private PythonData[][] points;

    private Mesh mesh;
    private Vector3[] vertices;
    private int[] triangles;

    private double totalProcessTime = 0;
    private float processTimes = 0;

    private bool meshDirty = false;

    private async void Start()
    {
        InitializePoints();
        InitializeMesh();

        client = new TcpClient();

        await client.ConnectAsync("127.0.0.1", 5000);

        NetworkStream stream = client.GetStream();
        reader = new StreamReader(stream);

        _ = ReceiveData();
    }

    private void InitializePoints()
    {
        points = new PythonData[GridSize][];

        for (int i = 0; i < GridSize; i++)
        {
            points[i] = new PythonData[GridSize];
        }
    }

    private void InitializeMesh()
    {
        mesh = new Mesh();

        // 256 * 256 = 65536 vertices, so UInt32 indices are required
        mesh.indexFormat = IndexFormat.UInt32;

        vertices = new Vector3[GridSize * GridSize];

        for (int i = 0; i < GridSize; i++)
        {
            for (int j = 0; j < GridSize; j++)
            {
                int index = GetVertexIndex(i, j);

                vertices[index] = Vector3.zero;
            }
        }

        triangles = new int[(GridSize - 1) * (GridSize - 1) * 6];

        int triangleIndex = 0;

        for (int i = 0; i < GridSize - 1; i++)
        {
            for (int j = 0; j < GridSize - 1; j++)
            {
                int bottomLeft = GetVertexIndex(i, j);
                int bottomRight = GetVertexIndex(i, j + 1);
                int topLeft = GetVertexIndex(i + 1, j);
                int topRight = GetVertexIndex(i + 1, j + 1);

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
        while (client.Connected)
        {
            string message = await reader.ReadLineAsync();

            if (message == null)
                break;

            Stopwatch stopwatch = Stopwatch.StartNew();

            PythonFrame frame =
                JsonUtility.FromJson<PythonFrame>(message);

            foreach (PythonData data in frame.points)
            {
                points[data.i][data.j] = data;

                int index = GetVertexIndex(data.i, data.j);

                vertices[index] = new Vector3(
                    data.x * 0.01f,
                    data.y,
                    data.z * 0.01f
                );
            }

            stopwatch.Stop();

            processTimes++;
            totalProcessTime += stopwatch.Elapsed.TotalMilliseconds;

            UnityEngine.Debug.Log(
                $"Frame Average Time Processing: {totalProcessTime / processTimes:F2} ms"
            );

            meshDirty = true;
        }
    }

    private void Update()
    {
        if (!meshDirty)
            return;

        //Stopwatch stopwatch = Stopwatch.StartNew();

        //mesh.vertices = vertices;

        //mesh.RecalculateNormals();
        //mesh.RecalculateBounds();

        //stopwatch.Stop();

        //UnityEngine.Debug.Log(
        //        $"Mesh Processing Ticks: {stopwatch.ElapsedTicks:F2}"
        //    );

        meshDirty = false;
    }

    private int GetVertexIndex(int i, int j)
    {
        return i * GridSize + j;
    }
}