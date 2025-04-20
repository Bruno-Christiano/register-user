from sqlalchemy.ext.asyncio import AsyncSession
from models.person import Person
from dtos.person_dto import CreatePersonDto,PersonResponseDto

async def create_person(db: AsyncSession, person_dto: CreatePersonDto) -> PersonResponseDto:
    person = Person(**person_dto.model_dump())
    db.add(person)
    await db.commit()
    await db.refresh(person)

    return PersonResponseDto.model_validate(person)
