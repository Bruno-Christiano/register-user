class PersonNotFoundError(Exception):
    def __init__(self, enrolment: int):
        self.enrolment = enrolment
        self.message = f"Pessoa com matrícula {enrolment} não encontrada."
        super().__init__(self.message)


class PersonIsExistingWithEnrolment(Exception):
    def __init__(self):
        self.message = "Matrícula ja cadastrada!"
        super().__init__(self.message)
