from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from server.database import get_async_db
from server.models import Course
from server.utils.response import make_records_response, make_response
from server.errors import ServerError

from .schemas import CourseAddIn, CourseFilterIn, CourseUpdateIn
from .schemas import CourseOutResponse, CourseListOutResponse

from .router import router
from server.utils.pagination import paginate


@router.get('/course/course-list', response_model=CourseListOutResponse)
async def get_course_list(db: AsyncSession = Depends(get_async_db), filter: CourseFilterIn = Query()):
    statement = select(Course)
    statement = paginate(statement, page=filter.page, size=filter.size)
    result = await db.execute(statement)
    course_list = result.scalars().all()

    statement = select(func.count()).select_from(Course)
    result = await db.execute(statement)
    total = result.scalar() or 0

    return make_records_response(records=course_list, total=total, page=filter.page, size=filter.size)


@router.get('/course/{id}', response_model=CourseOutResponse)
async def get_course_by_id(id: int, db: AsyncSession = Depends(get_async_db)):
    statement = select(Course).where(Course.id == id)
    result = await db.execute(statement)
    course = result.scalar_one_or_none()
    if not course:
        raise ServerError('找不到课程')

    return make_response(data=course)
