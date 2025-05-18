from typing import Optional

from sqlalchemy import Column, ForeignKeyConstraint, Index, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlmodel import Field, Relationship, SQLModel

class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, sa_column=Column('id', INTEGER(11), primary_key=True, comment='主键'))
    name: str = Field(sa_column=Column('name', String(255), comment='课程名称'))


class User(SQLModel, table=True):
    __table_args__ = (
        Index('username_unique', 'username', unique=True),
    )

    id: Optional[int] = Field(default=None, sa_column=Column('id', INTEGER(11), primary_key=True, comment='主键'))
    username: str = Field(sa_column=Column('username', String(255), comment='用户名'))
    password_hash: str = Field(sa_column=Column('password_hash', String(255)))


class UserCourseRelation(SQLModel, table=True):
    __tablename__ = 'user_course_relation'
    __table_args__ = (
        ForeignKeyConstraint(['course_id'], ['course.id'], ondelete='CASCADE', name='course_id_fk'),
        ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE', name='user_id_fk'),
        Index('course_id_fk', 'course_id'),
        Index('user_id_fk', 'user_id')
    )

    id: int = Field(sa_column=Column('id', INTEGER(11), primary_key=True, comment='主键'))
    user_id: int = Field(sa_column=Column('user_id', INTEGER(11), comment='用户id'))
    course_id: int = Field(sa_column=Column('course_id', INTEGER(11), comment='课程id'))

    course: Optional['Course'] = Relationship()
    user: Optional['User'] = Relationship()
