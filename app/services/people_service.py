# app/services/people_service.py
from dtos.person_dto import CreatePersonDto, PersonResponseDto
from typing import List
from models.errorMessage import ErrorMessage
from repostorieis import person_repository
from sqlalchemy.ext.asyncio import AsyncSession

async def create_person_service(db:AsyncSession, person_dto: CreatePersonDto) -> PersonResponseDto:
    created_person = await person_repository.create_person(db, person_dto)
    return created_person
