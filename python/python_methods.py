def print_text_type():
    print(type("Nakul"))  # <class 'str'>


def print_numeric_types():
    print(type(10))  # <class 'int'>
    print(type(30.5))  # <class 'float'>
    print(type(1 + 2j))  # <class 'complex'>


def print_sequence_types():
    print(type([1, 2, 3]))  # <class 'list'>
    print(type((1, 2, 3)))  # <class 'tuple'>
    print(type(range(5)))  # <class 'range'>


def print_mapping_type():
    print(type({"name": "John", "age": 30}))  # <class 'dict'>


def print_set_types():
    print(type({1, 2, 3}))  # <class 'set'>
    print(type(frozenset({1, 2})))  # <class 'frozenset'>


def print_boolean_type():
    print(type(True))  # <class 'bool'>
    print(type(False))  # <class 'bool'>


def print_binary_types():
    print(type(b'hello'))  # <class 'bytes'>
    print(type(bytearray(b'hello')))  # <class 'bytearray'>
    print(type(memoryview(b'hello')))  # <class 'memoryview'>


def print_none_type():
    print(type(None))  # <class 'NoneType'>


print_text_type()
print_numeric_types()
print_sequence_types()
print_mapping_type()
print_set_types()
print_boolean_type()
print_binary_types()
print_none_type()
