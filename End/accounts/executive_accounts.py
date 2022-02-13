from accounts.abc_accounts import Accounts
from employee_model import EmployeeModel
from applicants.abc_applicant_model import ApplicantModel

class ExecutiveAccounts(Accounts):
    def create(self, person: ApplicantModel):
        output = EmployeeModel()
        output.first_name = person.first_name
        output.last_name = person.last_name
        output.email_address = f"{person.first_name}.{person.last_name}@acmecorp.com"
        output.is_manager = True
        output.is_executive = True
        
        return output
