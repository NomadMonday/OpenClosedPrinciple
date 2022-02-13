from applicants.abc_applicant_model import ApplicantModel
from accounts.manager_accounts import ManagerAccounts

class ManagerModel(ApplicantModel):
    AccountProcessor = ManagerAccounts
