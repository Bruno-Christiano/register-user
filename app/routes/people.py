# app/routes/people.py
from fastapi import APIRouter, Depends, HTTPException
from services.people_service import (
    create_person_service,
    get_all_people_service,
    get_people_by_enrolment_service,
)
from dtos.person_dto import PersonResponseDto, CreatePersonDto
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from exceptions.personNotFound import (
    PersonNotFoundError,
    PersonIsExistingWithEnrolment,
)

router = APIRouter(prefix="", tags=["People"])


@router.post(
    "/createPerson",
    response_model=PersonResponseDto,
    summary="Create a new person",
    description="This endpoint creates a new person in the database.",
)
async def create_person_controller(
    person: CreatePersonDto, db: AsyncSession = Depends(get_db)
) -> PersonResponseDto:
    try:
        person = await create_person_service(db, person)
        return person
    except PersonIsExistingWithEnrolment as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.get(
    "/listAllPeople",
    response_model=list[PersonResponseDto],
    summary="Get all people",
    description="This endpoint retrieves all people from the database.",
)
async def get_all_people_controller(
    db: AsyncSession = Depends(get_db),
) -> list[PersonResponseDto]:
    return await get_all_people_service(db)


@router.get(
    "/getPeopleByEnrolment/{id}",
    response_model=PersonResponseDto,
    summary="Get People by enrolment",
    description="This endpoint retrieves one people from the database for .",
)
async def get_one_people_by_enrolment_controller(
    id: int,
    db: AsyncSession = Depends(get_db),
) -> PersonResponseDto:
    try:
        person = await get_people_by_enrolment_service(db, id)
        return person
    except PersonNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
