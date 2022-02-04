from abc_applicant_model import ApplicantModel
import manager_accounts

class ManagerModel(ApplicantModel):
    def create_account(self):
        return manager_accounts.create_manager_account(self)
