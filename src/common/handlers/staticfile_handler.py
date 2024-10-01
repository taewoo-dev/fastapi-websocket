from fastapi.staticfiles import StaticFiles


def attach_static_file_handlers(app):
    app.mount("/static", StaticFiles(directory="resources/static"), name="static")
