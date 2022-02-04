from employee_model import EmployeeModel
from person_model import PersonModel

def create_account(person: PersonModel):
    output = EmployeeModel()
    output.first_name = person.first_name
    output.last_name = person.last_name
    output.email_address = f"{person.first_name[0]}{person.last_name}@acme.com"
    
    return output
