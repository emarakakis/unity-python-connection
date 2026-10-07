import socket
import time
import math
import time
from pydantic import BaseModel

HOST = "127.0.0.1"
PORT = 5000

GRID_DIMENSION = 512


class Point(BaseModel):
    i: int
    j: int
    x: float
    y: float
    z: float


class Frame(BaseModel):
    points: list[Point]


def ChangePoints(points):
    current_time = time.time()

    for point in points:
        point.y = (
            math.sin(
                point.i * 0.08 +
                point.j * 0.08 +
                current_time * 2.0
            )
            * 0.2
        )


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Waiting for Unity...")

conn, addr = server.accept()
print("Unity connected:", addr)


points = [
    Point(
        i=i,
        j=j,
        x=i,
        y=0,
        z=j
    )
    for i in range(GRID_DIMENSION)
    for j in range(GRID_DIMENSION)
]


while True:
    # Give or take 30 frames per second
    time.sleep(0.05)
    ChangePoints(points)

    frame = Frame(points=points)

    message = frame.model_dump_json() + "\n"
    
    conn.sendall(message.encode("utf-8"))