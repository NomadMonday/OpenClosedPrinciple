from abc import ABC, abstractmethod

class Accounts(ABC):
    @abstractmethod
    def create(self, person):
        pass
