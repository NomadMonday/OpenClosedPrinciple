from abc import ABC, abstractmethod

class ApplicantModel(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @abstractmethod
    def create_account(self):
        pass
