from applicants.abc_applicant_model import ApplicantModel
from accounts.staff_accounts import create_staff_account

class PersonModel(ApplicantModel):
    def create_account(self):
        return create_staff_account(self)
