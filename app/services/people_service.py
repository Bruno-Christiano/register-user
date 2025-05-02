# app/services/people_service.py
from dtos.person_dto import CreatePersonDto, PersonResponseDto
from typing import List
from models.errorMessage import ErrorMessage
from repostorieis import person_repository
from sqlalchemy.ext.asyncio import AsyncSession
from exceptions.personNotFound import PersonNotFoundError, PersonIsExistingWithEnrolment


async def create_person_service(db: AsyncSession, person_dto: CreatePersonDto) -> PersonResponseDto:
    exist_people = await person_repository.get_people_by_enrolment(db, person_dto.enrolment)

    if exist_people:
        raise PersonIsExistingWithEnrolment()

    created_person = await person_repository.create_person(db, person_dto)
    return created_person


async def get_all_people_service(db: AsyncSession) -> List[PersonResponseDto]:
    people = await person_repository.get_all_people(db)
    if not people:
        return []
    # Transform the list of PersonResponseDto to a list of dictionaries
    return people


async def get_people_by_enrolment_service(db: AsyncSession, enrolment: int) -> PersonResponseDto | None:
    person = await person_repository.get_people_by_enrolment(db, enrolment)
    if not person:
        raise PersonNotFoundError(enrolment)
    return person
