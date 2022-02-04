from applicants.abc_applicant_model import ApplicantModel
from accounts.manager_accounts import create_manager_account

class ManagerModel(ApplicantModel):
    def create_account(self):
        return create_manager_account(self)
