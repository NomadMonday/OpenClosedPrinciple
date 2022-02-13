from applicants.abc_applicant_model import ApplicantModel
from accounts.staff_accounts import StaffAccounts

class PersonModel(ApplicantModel):
    AccountProcessor = StaffAccounts
