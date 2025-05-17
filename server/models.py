from typing import Optional

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, sa_column=Column('id', INTEGER(11), primary_key=True, comment='主键'))
    username: str = Field(sa_column=Column('username', String(255), comment='用户名'))
    password_hash: str = Field(sa_column=Column('password_hash', String(255)))
