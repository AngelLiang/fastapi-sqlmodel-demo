from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from server.database import get_async_db
from server.models import User
from server.utils.response import make_records_response, make_response
from server.errors import ServerError

from .schemas import UserAddIn, UserFilterIn, UserUpdateIn
from .schemas import UserOutResponse, UserListOutResponse

from .router import router
from server.utils.pagination import paginate


@router.get('/user-list', response_model=UserListOutResponse)
async def get_user(db: AsyncSession = Depends(get_async_db), filter: UserFilterIn = Query()):
    statement = select(User)
    statement = paginate(statement, page=filter.page, size=filter.size)
    result = await db.execute(statement)
    users = result.scalars().all()

    statement = select(func.count()).select_from(User)
    result = await db.execute(statement)
    total = result.scalar() or 0

    return make_records_response(records=users, total=total, page=filter.page, size=filter.size)


@router.post('/user', response_model=UserOutResponse)
async def add_user(payload: UserAddIn, db: AsyncSession = Depends(get_async_db)):
    db_user = User.model_validate(payload)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return make_response(db_user)


@router.put('/user/{id}', response_model=UserOutResponse)
async def update_user(id: int, payload: UserUpdateIn, db: AsyncSession = Depends(get_async_db)):
    # 先根据id查询用户
    statement = select(User).where(User.id == id)
    result = await db.execute(statement)
    db_user = result.scalar_one_or_none()

    if not db_user:
        raise ServerError(message=f"用户ID {id} 不存在")

    # 更新用户信息
    db_user.username = payload.username
    db_user.password_hash = payload.password_hash

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return make_response(db_user)


@router.get('/error')
async def error():
    raise ServerError()
