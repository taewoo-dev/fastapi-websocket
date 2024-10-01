from fastapi import WebSocket


class WebsocketConnectionManager:
    def __init__(self):
        """방 이름을 키로 하여 WebSocket 연결을 관리"""
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self, room: str, websocket: WebSocket):
        """클라이언트가 WebSocket을 통해 연결되면 이를 저장."""
        await websocket.accept()
        if room not in self.active_connections:
            self.active_connections[room] = []
        self.active_connections[room].append(websocket)
        await self.broadcast(room, "새로운 참가자가 들어왔습니다")

    def disconnect(self, room: str, websocket: WebSocket):
        """클라이언트가 연결을 종료할 때 호출되어 리스트에서 제거."""
        if room in self.active_connections:
            self.active_connections[room].remove(websocket)
            if len(self.active_connections[room]) == 0:
                del self.active_connections[room]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        """특정 클라이언트에게 메시지를 전송."""
        await websocket.send_text(message)

    async def broadcast(self, room: str, message: str):
        """특정 방에 연결된 모든 클라이언트에게 메시지를 브로드캐스트."""
        if room in self.active_connections:
            for connection in self.active_connections[room]:
                await connection.send_text(message)
