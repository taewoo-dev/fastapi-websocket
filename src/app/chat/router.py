from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
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
    """
    채팅방 화면을 렌더링
    """
    room = request.query_params.get("room", "default")
    return templates.TemplateResponse("chat.html", {"request": request, "room": room})


@router.websocket("/ws/{room_id}")
async def websocket_handler(websocket: WebSocket, room_id: str):
    """
    방별 WebSocket 핸들러
    """
    await manager.connect(room_id, websocket)

    try:
        await manager.broadcast(room_id, f"클라이언트가 {room_id} 방에 입장하였습니다.")

        while True:
            # 클라이언트로부터 메시지 수신
            data = await websocket.receive_text()

            # 방에 있는 다른 클라이언트에게 메시지 전송
            await manager.broadcast(room_id, f"메시지: {data}")

    except WebSocketDisconnect:
        # 클라이언트가 연결을 끊을 때 처리
        manager.disconnect(room_id, websocket)
        await manager.broadcast(room_id, f"클라이언트가 {room_id} 방을 떠났습니다.")

    except Exception as e:
        # 다른 예외 처리
        manager.disconnect(room_id, websocket)
        await manager.broadcast(room_id, f"에러 발생: {e}")
        raise e
