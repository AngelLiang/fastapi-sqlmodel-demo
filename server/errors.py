from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


class ServerError(Exception):
    def __init__(self, message="未知错误"):
        self.message = message
        super().__init__(self.message)


def init_exception_handler(app: FastAPI):

    @app.exception_handler(ServerError)
    async def handle_error(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=200,
            content={"code": 400, "message": exc.message, "data": {}},
        )
