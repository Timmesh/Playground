# Text Type: str
print(type("Nakul"))  # <class 'str'

# Numeric Types: int, float, complex
print(type(10))  # <class 'int'>
print(type(30.5))  # <class 'float'>
print(type(1 + 2j))  # <class 'complex'>

# Sequence Types: list, tuple, range
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type(range(5)))   # <class 'range'>

# Mapping Type: dict
print(type({"name": "John", "age": 30}))  # <class 'dict'>

# Set Types: set, frozenset
print(type({1, 2, 3}))        # <class 'set'>
print(type(frozenset({1, 2})))  # <class 'frozenset'>

# Boolean Type: bool
print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>

# Binary Types: bytes, bytearray, memoryview
print(type(b'hello'))          # <class 'bytes'>
print(type(bytearray(b'hello')))  # <class 'bytearray'>
print(type(memoryview(b'hello'))) # <class 'memoryview'>

# None Type: NoneType
print(type(None))  # <class 'NoneType'>
