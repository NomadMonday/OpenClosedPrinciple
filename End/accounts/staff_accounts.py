from employee_model import EmployeeModel
from applicants.abc_applicant_model import ApplicantModel

def create_staff_account(person: ApplicantModel):
    output = EmployeeModel()
    output.first_name = person.first_name
    output.last_name = person.last_name
    output.email_address = f"{person.first_name[0]}{person.last_name}@acme.com"
    
    return output
