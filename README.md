```markdown
# Unity - Python Connection

This project contains a simple TCP connection between Python and Unity.

## How to Run

1. Start the Python application first:

```bash
python main.py
```

The Python application will start the TCP server and wait for Unity to connect.

2. Open the Unity project.

3. Press **Play** in Unity.

Unity will connect to the Python server at:

```text
127.0.0.1:5000
```

## Important

Always run the applications in this order:

```text
1. Python
2. Unity
```

If Unity is started before the Python server, the connection will fail.
```