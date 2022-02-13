from applicants.abc_applicant_model import ApplicantModel
from accounts.executive_accounts import ExecutiveAccounts

class ExecutiveModel(ApplicantModel):
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._account_processor = ExecutiveAccounts()
    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def account_processor(self):
        return self._account_processor
