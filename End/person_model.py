from abc_applicant_model import ApplicantModel
import accounts

class PersonModel(ApplicantModel):
    def create_account(self):
        return accounts.create_account(self)
