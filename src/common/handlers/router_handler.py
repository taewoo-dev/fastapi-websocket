from app.chat.router import router as chat_router


def attach_router_handlers(app):
    app.include_router(router=chat_router)
