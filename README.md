# Back to basic Python

## Introduction
This repository is a collection of Python knowledge that I have learned from various sources. The main purpose of this repository is to help me to remember the basic Python knowledge that I have learned.
1. [Object Oriented Programming <python3.info>](https://python3.info/advanced/index.html#oop)
2. [Refactor Code <refactoring.guru>](https://refactoring.guru/refactoring/techniques)
3. [Design Patterns <refactoring.guru>](https://refactoring.guru/design-patterns/python)

## Object Oriented Programming
### Attributes
Attributes are the characteristics of an object. They are data stored inside a class or instance and represent the state or quality of the class or instance. In short, attributes store information about the instance.

#### Mutable vs Immutable
- Immutable Types: `int`, `float`, `complex`, `bool`, `None`, `str`, `bytes`, `tuple`, `frozenset`, `mappingproxy`
- Mutable Types: `list`, `set`, `dict`

Function and method arguments should not be mutable.

Details in [object-oriented-programming/attribute_mutable_immutable.py](https://github.com/vnk8071/python-space/blob/main/object-oriented-programming/attribute_mutable_immutable.py) file.

#### Class Variable vs Instance Variable
- Class Variable: Shared by all instances of the class (global variable)
```python
class User
    first_name = 'Khoi'
    last_name = 'VN'
```
- Instance Variable: Unique to each instance (__init__ method)
```python
class User
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
```

Details in [object-oriented-programming/class_variable_instance_variable.py](https://github.com/vnk8071/python-space/blob/main/object-oriented-programming/class_variable_instance_variable.py) file.

#### Annotations
Annotations are used to provide type hints to functions and methods. They are not enforced by the interpreter, but they can be used by external tools such as linters, IDEs, and type checkers.

```python
class User:
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
```
Details in [object-oriented-programming/class_variable_instance_variable.py](https://github.com/vnk8071/python-space/blob/main/object-oriented-programming/class_variable_instance_variable.py) file.

#### Slots
Slots are used to explicitly declare data members and deny the creation of `__dict__` and `__weakref__` (save memory). It is only available for new-style classes.

```python
class User:
    __slots__ = ['first_name', 'last_name']

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
```
Details in [object-oriented-programming/attribute_slots.py](https://github.com/vnk8071/python-space/blob/main/object-oriented-programming/attribute_slots.py) file.

### Property Decorator
Property is a special kind of attribute that computes its value when accessed. It is used to implement getters and setters.

```python
class User:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, value: str) -> None:
        self.first_name, self.last_name = value.split(' ', 1)
```
Details in [object-oriented-programming/property_decorator.py](https://github.com/vnk8071/python-space/blob/main/object-oriented-programming/property_decorator.py) file.

### Methods
#### Method Types
- Instance Method: It is bound to an instance of a class. It can access the instance through `self`.
- Static Method: It is bound to a class rather than its object. It does not require a class instance creation. It is not dependent on the state of the object.
- Class Method: It is bound to a class rather than its object. It can access the class through `cls`.
```python
class User:
    def instance_method(self) -> None:
        return 'instance method'

    @staticmethod
    def static_method() -> None:
        return 'static method'

    @classmethod
    def class_method(cls) -> None:
        return 'class method'
```
Details in [object-oriented-programming/method_in_class.py](https://github.com/vnk8071/python-space/blob/main/object-oriented-programming/method_in_class.py) file.

#### Static Method
Static method is a method that is bound to a class rather than its object. It does not require a class instance creation. It is not dependent on the state of the object.

```python
class User:
    def full_name_static_function(first_name: str, last_name: str) -> str:
        return f'{first_name} {last_name}'

    @staticmethod
    def full_name_static_method(first_name: str, last_name: str) -> str:
        return f'{first_name} {last_name}'
```
Details in [object-oriented-programming/method_staticmethod.py](https://github.com/vnk8071/python-space/blob/main/object-oriented-programming/method_staticmethod.py) file.

#### Class Method
Class method is a method that is bound to a class rather than its object. It can access the class through `cls`.

```python
class User:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_string: str) -> User:
        first_name, last_name = name_string.split(' ', 1)
        return cls(first_name, last_name)
```
Details in [object-oriented-programming/method_classmethod.py](https://github.com/vnk8071/python-space/blob/main/object-oriented-programming/method_classmethod.py) file.
