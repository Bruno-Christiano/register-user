# app/db/init_db.py
# db/init_db.py
from db.database import engine
from db.base import Base


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
