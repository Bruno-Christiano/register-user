from sqlalchemy.ext.asyncio import AsyncSession
from models.person import Person
from dtos.person_dto import CreatePersonDto, PersonResponseDto
from sqlalchemy.future import select
from typing import List
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError


async def create_person(db: AsyncSession, person_dto: CreatePersonDto) -> PersonResponseDto:

    person = Person(**person_dto.model_dump())
    db.add(person)
    await db.commit()
    await db.refresh(person)

    return PersonResponseDto.model_validate(person)


async def get_all_people(db: AsyncSession) -> List[PersonResponseDto]:
    result = await db.execute(select(Person))
    people = result.scalars().all()
    return [PersonResponseDto.model_validate(person) for person in people]


async def get_people_by_enrolment(db: AsyncSession, enrolment: int) -> PersonResponseDto | None:
    result = await db.execute(select(Person).where(Person.enrolment == enrolment))
    person = result.scalars().first()
    if person is None:
        return None
    return PersonResponseDto.model_validate(person)
