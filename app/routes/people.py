# app/routes/people.py
from fastapi import APIRouter
from app.models.person import Person
from app.services.people_service import list_people_service, create_person_service, delete_person_service_by_id

router = APIRouter(prefix="", tags=["People"])

@router.get("/listPeople", summary="List all people",description="This endpoint returns a list of all people in the database.")
def list_people():
    return list_people_service()

@router.post("/createPerson", summary="Create a new person", description="This endpoint creates a new person in the database.")
def create_person(person: Person):
    return create_person_service(person)
  
@router.delete("/deletePersonById/{id}", summary="Delete Person", description="This endpoint Delete person in the database.")
def delete_person(id: int):
    return delete_person_service_by_id(id)