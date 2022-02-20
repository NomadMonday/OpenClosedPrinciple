## Summary
- I created this project as a demonstration of the Open Closed Principle (the O in SOLID).
- It is a recreation of this demonstration by Tim Corey, except rewritten in Python: https://youtu.be/VFlk43QGEgc
- I wanted to create a semi-guided exercise where the objective is known, but the exact solution is not due to language differences. In this way, I could create a more challenging and engaging problem to solve, while also learning how to apply SOLID principles in Python.
- The Begin folder contains the starting point of the code before the principle is applied, and the End folder contains the refactored code after.

## Notes
#### The Python standard library does not use interfaces.
- Since the Python standard library does not have interfaces, the Open Closed Principle must be applied in a slightly different way compared to C#. (*To note, there are ways to implement interfaces in Python with libraries such as zope.interface. However, I wanted to stick to more core implementations, using the standard library whenever possible.*)
- Instead of interfaces, abstract base classes can be used in Python to allow for open extension. This allows us to create a "contract" of what to expect from a class, while leaving the details up to the inherited class's implementation.
- A key difference is that abstract base classes use a parent-child inheritance relationship rather than the interface implementation. Because of this, I was able to simplify the constructor of the applicant model classes to inherit from the base class, and only needed to define how to create accounts from each model.

#### Python is not strongly typed.
- Since Python is not strongly typed, there is less binding to the base class's "contract" as compared to an interface in C#.
- This difference was highlighted when I was figuring out how to implement the IAccounts AccountProcessor within the IApplicantModel, as defined here in C#:
```C#
public interface IApplicantModel
{
  string FirstName { get; set; }
  string LastName { get; set; }
  IAccounts AccountProcessor { get; set; }
}
```
- I initially tried to mimic the C# implementation, like so:
```Python
class ApplicantModel(ABC):
    @abstractmethod
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_processor = Accounts()
```
- However, this meant I had to override the constructor in each implementation, and the connection from ApplicantModel to the account_processor to the Accounts class was perhaps too.. abstract? (pun intended?) One could easily forget to assign the account_processor in the overridden constructor since it's not in the constructor parameter definition.
- A realization I had, though, was that everything in Python is an object, even class definitions. Meaning, I could assign a class definition to a variable. Furthermore, Python classes can have class variables, and so I could have a class variable that is assigned the definition of a class, like this:
```Python
class ApplicantModel(ABC):
    AccountProcessor = Accounts
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_processor = self.AccountProcessor()
```
- And so, AccountProcessor must be overridden since Accounts is an abstract base class. However, I can still have child classes inherit the parent constructor, like so:
```Python
class PersonModel(ApplicantModel):
    AccountProcessor = StaffAccounts
```
- This implementation has more implicit enforcement of the account_processor property and has it more strongly connected to the Accounts abstract base class.
