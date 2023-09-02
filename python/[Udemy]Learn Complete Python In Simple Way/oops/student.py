class Student:
    '''Developed for Python demo'''

    def __init__(self):
        self.name = 'Nakul'
        self.age = 40
        self.marks = 80

    def talk(self):
        print("Hello, I am:", self.name)
        print("My Age is:", self.age)
        print("My Marks are:", self.marks)

help(Student)
print(Student.__doc__)