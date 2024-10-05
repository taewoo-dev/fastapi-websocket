from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from common.post_construct import post_construct


app = FastAPI()

post_construct(app)

templates = Jinja2Templates(directory="resources/templates")


@app.get("/", response_class=HTMLResponse)
async def root_handler(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
