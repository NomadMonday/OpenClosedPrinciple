from accounts import create_account
from employee_model import EmployeeModel
from person_model import PersonModel

def main():
    applicants = [
        PersonModel("Tim", "Corey"),
        PersonModel("Sue", "Storm"),
        PersonModel("Nancy", "Roman")
    ]

    employees = [create_account(applicant) for applicant in applicants]

    for employee in employees:
        print(f"{employee.FirstName} {employee.LastName}: {employee.EmailAddress} IsManager: {employee.IsManager} IsExecutive: {employee.IsExecutive}")
    
    input()

if __name__ == "__main__":
    main()
