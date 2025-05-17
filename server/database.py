from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool, AsyncAdaptedQueuePool

from server.settings import ASYNC_DATABASE_URL


# 创建异步引擎, 使用连接池, 连接池配置
engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,
    poolclass=NullPool,
    # pool_pre_ping=True,  # 在每次连接前ping一下确保连接有效
    # pool_size=20,  # 增加连接池大小
    # max_overflow=30,  # 增加最大溢出连接数
    # pool_timeout=30,  # 池连接超时时间
    # pool_recycle=1800,  # 连接回收时间(秒)
)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()


async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session


async_session = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)
