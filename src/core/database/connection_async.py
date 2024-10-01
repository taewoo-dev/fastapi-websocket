from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.config import settings

# 데이터베이스에 접근,설정을 관리하는 객체
async_engine = create_async_engine(settings.database_url)

# 세션을 생성하는 객체
AsyncSessionFactory = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=async_engine,
)


# 의존성 주입을 위한 함수
async def get_async_db():
    session = AsyncSessionFactory()
    try:
        yield session
    finally:
        await session.close()
