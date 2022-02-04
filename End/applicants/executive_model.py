from applicants.abc_applicant_model import ApplicantModel
from accounts.executive_accounts import create_executive_account

class ExecutiveModel(ApplicantModel):
    def create_account(self):
        return create_executive_account(self)
