# app/routes/people.py
from fastapi import APIRouter
from services.people_service import create_person_service
from dtos.person_dto import PersonResponseDto, CreatePersonDto
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from fastapi import Depends
router = APIRouter(prefix="", tags=["People"])

@router.post("/createPerson", 
             response_model=PersonResponseDto, 
             summary="Create a new person", 
             description="This endpoint creates a new person in the database.")

async def create_person_controller(person: CreatePersonDto, db:AsyncSession = Depends(get_db)) -> PersonResponseDto:
    return await create_person_service(db,person)
  