from sqlmodel import SQLModel
from typing import List, Optional
from server.models import Course
from server.utils.schemas import make_response_schema, make_records_response_schema
from server.utils.schemas import to_camel_case


class CourseFilterIn(SQLModel):
    page: int | None = None
    size: int | None = None


class CourseAddIn(SQLModel):

    class Config:
        from_attributes = True
        populate_by_name = True
        # 将下划线命名转换为驼峰命名
        alias_generator = to_camel_case


class CourseUpdateIn(SQLModel):
    name: str

    class Config:
        from_attributes = True
        populate_by_name = True
        # 将下划线命名转换为驼峰命名
        alias_generator = to_camel_case


class CourseOut(SQLModel):
    id: Optional[int] = None
    name: str
    # 不包含 user_course_relation 字段，避免循环引用问题

    class Config:
        from_attributes = True
        populate_by_name = True
        # 将下划线命名转换为驼峰命名
        alias_generator = to_camel_case


CourseOutResponse = make_response_schema(CourseOut)
CourseListOutResponse = make_records_response_schema(CourseOut)
