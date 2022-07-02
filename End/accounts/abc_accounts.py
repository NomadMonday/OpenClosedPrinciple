from __future__ import annotations
from abc import ABC, abstractmethod
from employee_model import EmployeeModel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from applicants.abc_applicant_model import ApplicantModel

class Accounts(ABC):
    @abstractmethod
    def create(self, person: ApplicantModel) -> EmployeeModel:
        pass
