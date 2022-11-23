from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse, PlainTextResponse
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

from models.Settings import AppSettings

settings = AppSettings()

middleware = [
    Middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET)
]

app = FastAPI(middleware=middleware)


@app.get('/')
async def index(request: Request, status_code=status.HTTP_200_OK) -> RedirectResponse:
    if not request.session.get('username'):
        return RedirectResponse('/login')

    return RedirectResponse('/home')





if __name__ == '__main__':
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)