from employee_model import EmployeeModel
from person_model import PersonModel

def create_account(person: PersonModel):
    output = EmployeeModel()
    output.FirstName = person.FirstName
    output.LastName = person.LastName
    output.EmailAddress = f"{person.FirstName[0]}{person.LastName}@acme.com"
    
    return output
