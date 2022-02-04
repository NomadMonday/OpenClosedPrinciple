from accounts import create_account
from employee_model import EmployeeModel
from manager_model import ManagerModel
from person_model import PersonModel

def main():
    applicants = [
        PersonModel("Tim", "Corey"),
        ManagerModel("Sue", "Storm"),
        PersonModel("Nancy", "Roman")
    ]

    employees = [applicant.create_account() for applicant in applicants]

    for employee in employees:
        print(f"{employee.first_name} {employee.last_name}: {employee.email_address} IsManager: {employee.is_manager} IsExecutive: {employee.is_executive}")
    
    input()

if __name__ == "__main__":
    main()