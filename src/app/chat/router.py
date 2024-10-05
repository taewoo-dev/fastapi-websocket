from fastapi import APIRouter, WebSocket, Depends
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.websockets import WebSocketDisconnect

from app.chat.managers.web_socket_manager import WebsocketConnectionManager
from app.chat.services.message_service import MessageService
from app.chat.services.room_service import RoomService
from app.user.services.mock_user_service import MockUserService

# 라우터 설정
router = APIRouter(prefix="/chat", tags=["chat"])

manager = WebsocketConnectionManager()

templates = Jinja2Templates(directory="resources/templates")


@router.get("/", response_class=HTMLResponse)
async def chat(
    request: Request,
    room_service: RoomService = Depends(),
):
    """채팅방 화면을 렌더링"""
    room = request.query_params.get("room", "default")
    await room_service.save_room(room_name=room)
    return templates.TemplateResponse("chat.html", {"request": request, "room": room})


@router.websocket("/ws/{room_id}")
async def websocket_handler(
    websocket: WebSocket,
    room_id: str,
    message_service: MessageService = Depends(),
    mock_user_service: MockUserService = Depends(),
):
    """방별 WebSocket 핸들러"""
    user_id, user_name = await mock_user_service.generate_random_user()

    await manager.connect(room_id, websocket)

    try:
        while True:
            data = await websocket.receive_text()

            await message_service.save_message(
                room_id=room_id, user_id=user_id, content=data
            )

            await manager.broadcast(room_id, f"{user_name}: {data}")

    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
        await manager.broadcast(room_id, "클라이언트가 방을 떠났습니다")
