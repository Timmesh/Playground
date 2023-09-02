from abc import ABC, abstractmethod

class Test(ABC):
    # Case-1: Concrete class with no abstract methods
    def concrete_method(self):
        print("Concrete method in the concrete class")

# Case-2: Derived from ABC, but no abstract methods
class Test2(ABC):
    pass

# Case-3: Derived from ABC with an abstract method
class Test3(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Case-4: Concrete class with an abstract method (not recommended)
class Test4:
    @abstractmethod
    def abstract_method(self):
        pass

# Case-5: Derived from ABC with an abstract method
class Test5(ABC):
    @abstractmethod
    def abstract_method(self):
        print("Abstract method in the abstract class")

# Instantiate objects
t1 = Test()
# t2 = Test2()  # This line will raise a TypeError
# t3 = Test3()  # This line will raise a TypeError
# t4 = Test4()  # This line is allowed but not recommended
# t5 = Test5()  # This line will raise a TypeError
