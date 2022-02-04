from employee_model import EmployeeModel
from abc_applicant_model import ApplicantModel

def create_manager_account(person: ApplicantModel):
    output = EmployeeModel()
    output.first_name = person.first_name
    output.last_name = person.last_name
    output.email_address = f"{person.first_name[0]}{person.last_name}@acmecorp.com"
    output.is_manager = True
    
    return output
