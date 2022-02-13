from applicants.abc_applicant_model import ApplicantModel
from accounts.executive_accounts import ExecutiveAccounts

class ExecutiveModel(ApplicantModel):
    AccountProcessor = ExecutiveAccounts
