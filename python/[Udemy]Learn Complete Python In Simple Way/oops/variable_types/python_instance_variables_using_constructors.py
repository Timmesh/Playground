# Inside Constructor by using Self Variable:

# We can declare instance variables inside a constructor by using the self keyword. Once we create an object,
# these variables will be automatically added to the object.

class Employee:
    def __init__(self):
        self.eno = 100
        self.ename = 'Durga'
        self.esal = 10000

e = Employee()
print(e.__dict__)  # {'eno': 100, 'ename': 'Durga', 'esal': 10000}
