# Inner Classes Example

# The following code demonstrates the use of inner classes.

# Outer class definition
class Human:
    def __init__(self):
        self.name = 'Nakul'
        # Creating an instance of the inner class 'Head'
        self.head = self.Head()
        # Creating an instance of the inner class 'Brain'
        self.brain = self.Brain()

    def display(self):
        print("Hello..", self.name)

    # Inner class definition
    class Head:
        def talk(self):
            print('Talking...')

    # Another inner class definition
    class Brain:
        def think(self):
            print('Thinking...')

# Creating an instance of the outer class 'Human'
h = Human()

# Calling the method of the outer class to display the name
h.display()          # Hello.. Sunny

# Calling the method of the inner class 'Head'
h.head.talk()        # Talking...

# Calling the method of the inner class 'Brain'
h.brain.think()      # Thinking...
