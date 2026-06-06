from fastapi import WebSocket

class ClusterSocketManager:
    def __init__(self):
        self.connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def broadcast(self, message: str):
        for connection in self.connections:
            await connection.send_text(message)
