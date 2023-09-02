# Import the ABC (Abstract Base Class) module from the abc package
from abc import ABC, abstractmethod

# Define an abstract class DBInterface that extends ABC (making it an interface)
class DBInterface(ABC):
    # Define an abstract method connect() that should be implemented by subclasses
    @abstractmethod
    def connect(self):
        pass

    # Define an abstract method disconnect() that should be implemented by subclasses
    @abstractmethod
    def disconnect(self):
        pass

# Define a concrete class Oracle that implements the DBInterface interface
class Oracle(DBInterface):
    # Implement the connect() method for Oracle
    def connect(self):
        print('Connecting to Oracle Database...')

    # Implement the disconnect() method for Oracle
    def disconnect(self):
        print('Disconnecting from Oracle Database...')

# Define another concrete class Sybase that also implements the DBInterface interface
class Sybase(DBInterface):
    # Implement the connect() method for Sybase
    def connect(self):
        print('Connecting to Sybase Database...')

    # Implement the disconnect() method for Sybase
    def disconnect(self):
        print('Disconnecting from Sybase Database...')

# Prompt the user to enter a database name
dbname = input('Enter Database Name (Oracle or Sybase): ')

# Use globals() to dynamically fetch the class based on user input
# This allows us to create an instance of the selected database class
classname = globals()[dbname]
database = classname()

# Call the connect() and disconnect() methods on the selected database instance
database.connect()
database.disconnect()
