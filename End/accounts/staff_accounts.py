from accounts.abc_accounts import Accounts
from employee_model import EmployeeModel
from applicants.abc_applicant_model import ApplicantModel

class StaffAccounts(Accounts):
    def create(self, person: ApplicantModel) -> EmployeeModel:
        output = EmployeeModel()
        output.first_name = person.first_name
        output.last_name = person.last_name
        output.email_address = f"{person.first_name[0]}{person.last_name}@acme.com"
        
        return output
