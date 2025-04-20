# app/services/people_service.py
from app.models.person import Person
from typing import List
from app.models.errorMessage import ErrorMessage

# fake DB simulando armazenamento
_fake_db: List[Person] = []

def list_people_service():
    return _fake_db

def create_person_service(person: Person):
  
    if any(p.id == person.id for p in _fake_db):
      error_message = ErrorMessage(message="Pessoa já cadastrada!")
      return error_message

    if person.age < 18:
      error_message = ErrorMessage(message="Pessoa menor de idade não pode ser cadastrada!")
      return error_message
      
    elif person.age > 120: 
      error_message = ErrorMessage(message="Idade inválida!")
      return error_message
    
    _fake_db.append(person)
    return person
  
def delete_person_service_by_id(id: int):
    person_to_remove = next((person for person in _fake_db if person.id == id), None)
    
    if person_to_remove:
        _fake_db.remove(person_to_remove)
        error_message = ErrorMessage(message="Pessoa removida com sucesso!")
        return error_message
    else:
        error_message = ErrorMessage(message="Pessoa não encontrada!")
        return error_message
