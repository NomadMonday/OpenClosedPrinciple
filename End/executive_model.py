from abc_applicant_model import ApplicantModel
import executive_accounts

class ExecutiveModel(ApplicantModel):
    def create_account(self):
        return executive_accounts.create_executive_account(self)
