from pydantic import BaseModel, field_validator
from datetime import datetime
import re


class CreatePersonDto(BaseModel):
    name: str
    age: int
    enrolment: int

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value: str) -> str:

        if not value.strip():

            raise ValueError("Nome não pode estar em branco.")

        if value != value.strip():
            raise ValueError("Nome não pode começar ou terminar com espaços.")

        if value != value.strip():
            raise ValueError("Nome não pode começar ou terminar com espaços.")

        if len(value) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres.")

        if len(value) > 50:
            raise ValueError("Nome deve ter no máximo 50 caracteres.")

        return value

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, value: int) -> int:

        if value < 0:
            raise ValueError("Idade deve ser um número positivo.")

        if value > 120:
            raise ValueError("Idade inválida!")

        if value < 18:
            raise ValueError("Pessoa menor de idade não pode ser cadastrada!")

        return value

    @field_validator("enrolment")
    @classmethod
    def enrolment_must_be_positive(cls, value: int) -> int:

        if not isinstance(value, int):
            raise ValueError("Matrícula deve ser um número inteiro.")

        if value < 0:
            raise ValueError("Matrícula deve ser um número positivo.")

        if len(str(value)) > 8:
            raise ValueError("Matrícula deve ser no máximo 8 dígitos.")

        if re.match(r"^[0-9]+$", str(value)) is None:

            raise ValueError("Matrícula deve conter apenas números.")
        return value


class PersonResponseDto(BaseModel):
    id: int
    name: str
    age: int
    created_at: datetime
    updated_at: datetime
    enrolment: int
    model_config = {"from_attributes": True}
