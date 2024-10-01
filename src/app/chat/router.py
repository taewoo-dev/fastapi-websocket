from fastapi import APIRouter, WebSocket
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.websockets import WebSocketDisconnect

from app.chat.managers.web_socket_manager import WebsocketConnectionManager


# 라우터 설정
router = APIRouter(prefix="/chat", tags=["chat"])

manager = WebsocketConnectionManager()

templates = Jinja2Templates(directory="resources/templates")


@router.get("/", response_class=HTMLResponse)
async def chat(request: Request):
    """채팅방 화면을 렌더링"""
    room = request.query_params.get("room", "default")
    return templates.TemplateResponse("chat.html", {"request": request, "room": room})


@router.websocket("/ws/{room_id}")
async def websocket_handler(websocket: WebSocket, room_id: str):
    """방별 WebSocket 핸들러"""
    await manager.connect(room_id, websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(room_id, data)

    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
        await manager.broadcast(room_id, "클라이언트가 방을 떠났습니다")
