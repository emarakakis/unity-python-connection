import socket
import time
import numpy as np

HOST = "127.0.0.1"
PORT = 5000

GRID_SIZE = 512

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Waiting for Unity...")

conn, addr = server.accept()

print("Unity connected:", addr)

i, j = np.meshgrid(
    np.arange(GRID_SIZE),
    np.arange(GRID_SIZE),
    indexing="ij"
)

while True:
    frame_start = time.perf_counter()

    current_time = time.time()

    calculation_start = time.perf_counter()

    heights = np.sin(
        i * 0.08 +
        j * 0.08 +
        current_time * 2.0
    ).astype(np.float32) * 0.2

    calculation_end = time.perf_counter()

    conversion_start = time.perf_counter()

    data = heights.tobytes()

    conversion_end = time.perf_counter()

    send_start = time.perf_counter()

    conn.sendall(data)

    send_end = time.perf_counter()

    total_end = time.perf_counter()

    print(
        f"Size: {len(data) / 1024 / 1024:.2f} MiB | "
        f"Calculate: {(calculation_end - calculation_start) * 1000:.2f} ms | "
        f"ToBytes: {(conversion_end - conversion_start) * 1000:.2f} ms | "
        f"Send: {(send_end - send_start) * 1000:.2f} ms | "
        f"Total: {(total_end - frame_start) * 1000:.2f} ms"
    )