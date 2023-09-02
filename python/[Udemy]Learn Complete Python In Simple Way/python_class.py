class DataTypesPrinter:
    def print_text_type(self):
        print(type("Nakul"))  # <class 'str'>

    def print_numeric_types(self):
        print(type(10))  # <class 'int'>
        print(type(30.5))  # <class 'float'>
        print(type(1 + 2j))  # <class 'complex'>

    def print_sequence_types(self):
        print(type([1, 2, 3]))  # <class 'list'>
        print(type((1, 2, 3)))  # <class 'tuple'>
        print(type(range(5)))  # <class 'range'>

    def print_mapping_type(self):
        print(type({"name": "John", "age": 30}))  # <class 'dict'>

    def print_set_types(self):
        print(type({1, 2, 3}))  # <class 'set'>
        print(type(frozenset({1, 2})))  # <class 'frozenset'>

    def print_boolean_type(self):
        print(type(True))  # <class 'bool'>
        print(type(False))  # <class 'bool'>

    def print_binary_types(self):
        print(type(b'hello'))  # <class 'bytes'>
        print(type(bytearray(b'hello')))  # <class 'bytearray'>
        print(type(memoryview(b'hello')))  # <class 'memoryview'>

    def print_none_type(self):
        print(type(None))  # <class 'NoneType'>


printer = DataTypesPrinter()

printer.print_text_type()
printer.print_numeric_types()
printer.print_sequence_types()
printer.print_mapping_type()
printer.print_set_types()
printer.print_boolean_type()
printer.print_binary_types()
printer.print_none_type()
