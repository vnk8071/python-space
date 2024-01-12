"""Attribute class variables
- Fields defined on a class
- Must have default values
- Share state
- Also known as 'static attributes'

Author: Khoi VN
Date: 15/10/2023
"""


from typing import ClassVar
from dataclasses import dataclass
from src.logger import Logger


logger = Logger.get_logger(__name__)


# --------------------------------------------------
# User class var
# --------------------------------------------------
@dataclass
class UserClassVar:
    pass


UserClassVar.firstname = "Khoi"
UserClassVar.lastname = "VN"

assert UserClassVar.firstname == "Khoi"
assert UserClassVar.lastname == "VN"

logger.info(f"UserClassVar: {UserClassVar.firstname} {UserClassVar.lastname}")

"""Instance variables
- Fields defined on an instance
- Do not share state (unless mutable argument in method signature)
- By convention initialized in __init__()
- Also known as 'dynamic attributes'
"""


# --------------------------------------------------
# User instance var
# --------------------------------------------------
class UserInstanceVar:
    def __init__(self):
        self.firstname = "Khoi"
        self.lastname = "VN"


logger.info(
    f"UserInstanceVar: {UserInstanceVar().firstname} {UserInstanceVar().lastname}"
)

""" Class variables and instance variables
"""


@dataclass
class UserClassVarInstanceVar:
    firstname: ClassVar[str] = "Khoi"
    lastname: ClassVar[str] = "VN"

    def __init__(self):
        self.firstname = "Khoi"
        self.lastname = "VN"


"""Class variables vs instance variables
"""


class User:
    groups = ["admin", "user", "guest"]


khoivn = User()
kelvin = User()
assert khoivn.groups == ["admin", "user", "guest"]
assert kelvin.groups == ["admin", "user", "guest"]
logger.info(f"Group of khoivn: {khoivn.groups}")  # ['admin', 'user', 'guest']
logger.info(f"Group of kelvin: {kelvin.groups}")  # ['admin', 'user', 'guest']


User.groups = ["super_user"]
assert khoivn.groups == ["super_user"]
assert kelvin.groups == ["super_user"]
logger.info(f"Group of khoivn: {khoivn.groups}")  # ['super_user']
logger.info(f"Group of kelvin: {kelvin.groups}")  # ['super_user']

khoivn.groups = ["admin"]
assert khoivn.groups == ["admin"]
assert kelvin.groups == ["super_user"]
logger.info(f"Group of khoivn: {khoivn.groups}")  # ['admin']
logger.info(f"Group of kelvin: {kelvin.groups}")  # ['super_user']


User.groups = ["guest"]
assert khoivn.groups == ["admin"]
assert kelvin.groups == ["guest"]
logger.info(f"Group of khoivn: {khoivn.groups}")  # ['super_user', 'admin']
logger.info(f"Group of kelvin: {kelvin.groups}")  # ['guest']


# --------------------------------------------------
# User mechanism
# --------------------------------------------------
class UserMechanism:
    firstname = "Khoi"
    lastname = "VN"

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


khoivn = UserMechanism("Khoi", "VN")
assert vars(khoivn) == {"firstname": "Khoi", "lastname": "VN"}
logger.info(f"vars: {vars(khoivn)}")
# {'firstname': 'Khoi', 'lastname': 'VN'}
