from sqlmodel import SQLModel

from server.models import User
from server.utils.schemas import make_response_schema, make_records_response_schema
from server.utils.schemas import to_camel_case


class UserFilterIn(SQLModel):
    page: int | None = None
    size: int | None = None


class UserAddIn(SQLModel):
    username: str
    password_hash: str

    class Config:
        from_attributes = True
        populate_by_name = True
        # 将下划线命名转换为驼峰命名
        alias_generator = to_camel_case


class UserUpdateIn(SQLModel):
    username: str
    password_hash: str

    class Config:
        from_attributes = True
        populate_by_name = True
        # 将下划线命名转换为驼峰命名
        alias_generator = to_camel_case


class UserOut(User, table=False):
    class Config:
        from_attributes = True
        populate_by_name = True
        # 将下划线命名转换为驼峰命名
        alias_generator = to_camel_case


UserOutResponse = make_response_schema(UserOut)
UserListOutResponse = make_records_response_schema(UserOut)
