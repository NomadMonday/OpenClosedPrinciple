### Summary
- This project is a demonstration of the Open Closed Principle (the O in SOLID).
- It is a recreation of this demonstration by Tim Corey, except rewritten in Python: https://youtu.be/VFlk43QGEgc
- The purpose of this project was to create a semi-guided exercise, where the objective is defined, but the answer is not since it's in a different language. The challenge of the exercise being to learn how to apply SOLID principles in Python.
- The Begin folder contains the starting point of the code before the principle is applied, and the End folder contains the refactored code after.

### Notes
- Since Python typically doesn't implement interfaces, the Open Closed Principle must be applied in a slightly different way compared to C#.
  - More simply, inheritance can be used to allow for open extension. However, this still allows for the parent class to be used directly, violating the Open Closed Principle, and there are potential unintended consequences of a child class mistakenly invoking methods or properties from the super class.
  - Using abstract base classes, we can create a parent class that cannot be instantiated directly, and use abstract methods and properties to ensure child classes have their own implementation.
- There are different possible ways of approaching the IAccounts AccountProcessor within the IApplicantModel.
  - I initially translated the IAccounts class into a standalone function within an Accounts module. Since the only responsibility of the IAccounts class was to create the account, I didn't think having a class around it was necessary. This can be seen in my previous commit here: https://github.com/NomadMonday/OpenClosedPrinciple/tree/98a95462a1538942b09e5f77c0374f763112c534
  - I later modified it to mirror the original implementation with the account processor being a class and having it as a member of the applicant model. The thinking being that the account creation process is simplified for demonstration purposes, and that a real account processor might need the class structure around it.
  - One potential issue with this is that since Python isn't strongly typed, there's no guarantee that account_proccesor is actually an Account type that contains a create() method. Having the create_account() method directly in the ApplicantModel could potentially be a better implementation in Python, since it can be set as an abstract method and we can be assured of its existence.
