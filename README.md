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
  - I initially translated the IAccounts class into a standalone function within an Accounts module. Since the only responsibility of the IAccounts class was to create the account, I didn't think having a class around it was necessary. This can be seen in a previous commit here: https://github.com/NomadMonday/OpenClosedPrinciple/tree/98a95462a1538942b09e5f77c0374f763112c534
  - I later modified it in the following commit to mirror the original implementation, setting the account_processor as a property of the ApplicantModel. The reasoning behind this is that the account creation process is simplified for demonstration purposes, and a real account processor might actually need the class structure around it. https://github.com/NomadMonday/OpenClosedPrinciple/tree/677aca079a960641c9eaab98fb67cdedafb8ee8d
  - An issue I ran into with this is that since Python isn't strongly typed, there's no guarantee that account_proccesor is actually an Account type that contains a create() method, and abstract base classes do not allow for nested definitions the way interfaces do in C#.
  - However, since Python allows for the assignment of class definitions to a variable, I was able to devise a workaround by defining an AccountProcessor class attribute in the ApplicantModel abstract base class that contains the class definition of the Accounts abstract base class. The account_processor instance variable is then created from this class. This implicitly enforces the Accounts abstract base class and ensures the account_processor will now have a create() method.
