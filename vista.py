import numpy as np
import pyvista as pv
import time

points = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0]
], dtype=float)

faces = np.array([
    3, 0, 1, 2,
    3, 0, 2, 3
])

mesh = pv.PolyData(points, faces=faces)

plotter = pv.Plotter()
plotter.add_mesh(mesh, color="green", show_edges=True)
plotter.show(auto_close=False, interactive_update=True)

start = time.perf_counter()

while True:
    t = time.perf_counter() - start

    # Update only vertex positions
    mesh.points[:, 2] = np.array([
        0,
        np.sin(t),
        np.sin(t),
        0
    ])

    plotter.update()