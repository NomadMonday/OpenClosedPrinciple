from abc import ABC, abstractmethod
from accounts.abc_accounts import Accounts

class ApplicantModel(ABC):
    @abstractmethod
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._account_processor = Accounts()
    
    @property
    @abstractmethod
    def first_name(self):
        pass

    @first_name.setter
    @abstractmethod
    def first_name(self, value):
        pass

    @property
    @abstractmethod
    def last_name(self):
        pass

    @last_name.setter
    @abstractmethod
    def last_name(self, value):
        pass

    @property
    @abstractmethod
    def account_processor(self):
        pass