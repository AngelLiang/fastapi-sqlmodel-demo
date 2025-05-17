from fastapi import FastAPI


app = FastAPI(
    title="fastapi-sqlmodel-demo",
    # 禁用自动重定向
    redirect_slashes=False
)


from server.errors import init_exception_handler
init_exception_handler(app)


from server.user.router import init_user_router
init_user_router(app)
