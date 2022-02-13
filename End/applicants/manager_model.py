from applicants.abc_applicant_model import ApplicantModel
from accounts.manager_accounts import ManagerAccounts

class ManagerModel(ApplicantModel):
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._account_processor = ManagerAccounts()
    
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
