# app/db/database.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./people.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},echo=True)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# # Função que cria uma nova sessão para cada requisição
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

DATABASE_URL = "sqlite+aiosqlite:///./people.db"
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db():
    async with SessionLocal() as session:
        yield session
