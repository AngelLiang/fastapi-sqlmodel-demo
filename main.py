from fastapi import FastAPI
from pydantic import ConfigDict

app = FastAPI(
    title="fastapi-sqlmodel-demo",
    # 禁用自动重定向
    redirect_slashes=False
)

# 添加全局 Pydantic 配置
app.model_config = ConfigDict(
    arbitrary_types_allowed=True,
    from_attributes=True
)

from server.errors import init_exception_handler
init_exception_handler(app)


from server.user.router import init_user_router
init_user_router(app)


from server.course.router import init_course_router
init_course_router(app)
