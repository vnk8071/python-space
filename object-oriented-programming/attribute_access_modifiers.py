"""Attribute access modifiers
- Attributes and methods are always public
- No protected and private keywords
- Private and protected is only by convention [1]
- name - public attribute
- _name - protected attribute (non-public by convention)
- __name - private attribute (name mangling)
- __name__ - system attribute (dunder)
- name_ - avoid name collision with built-ins

Author: Khoi VN
Date: 15/10/2023
"""


from dataclasses import dataclass

from src.logger import Logger

logger = Logger.get_logger(__name__)


# --------------------------------------------------
# User modifiers
# --------------------------------------------------
class UserModifiers:
    firstname: str = "Khoi"  # public
    lastname: str = "VN"  # public
    _age: int = 23  # public, but... non-public by convention
    _email: str = "nguyenkhoi8071@"  # public, but... non-public by convention
    __address: str = "Quang Ngai"  # public, but... private by convention
    id_: int  # public, but... public, avoid name collision
    type_: str  # public, but... public, avoid name collision
    # public, but... special meaning built-in (dunder)
    __doc__: str
    # public, but... special meaning built-in (dunder)
    __module__: str
    # public, but... special meaning custom made (dunder)
    __version__: str
    # public, but... special meaning custom made (dunder)
    __author__: str


@dataclass
class UserExample:
    def __init__(self):
        self.firstname: str = "Khoi"
        self.lastname: str = "VN"
        self._age: int = 23
        self._email: str = "nguyenkhoi8071@"
        self.__address: str = "Quang Ngai"
        self.id_: int = 1
        self.type_: str = "admin"
        self.__doc__: str = "This is a user class"
        self.__module__: str = "__main__"
        self.__version__: str = "1.0.0"
        self.__author__: str = "Khoi VN"


# --------------------------------------------------
# User attribute
# --------------------------------------------------
@dataclass
class UserPublicAttribute:
    firstname: str
    lastname: str


khoivn = UserPublicAttribute("Khoi", "VN")
assert khoivn.firstname == "Khoi"
assert khoivn.lastname == "VN"
logger.info(f"UserPublicAttribute: {khoivn.firstname} {khoivn.lastname}")  # Khoi VN
logger.info(f"vars {vars(khoivn)}")
# {'firstname': 'Khoi', 'lastname': 'VN'}


@dataclass
class UserProtectedAttribute:
    _firstname: str
    _lastname: str


_khoivn = UserProtectedAttribute("Khoi", "VN")
assert _khoivn._firstname == "Khoi"
assert _khoivn._lastname == "VN"
# Khoi VN
logger.info(f"UserProtectedAttribute: {_khoivn._firstname} {_khoivn._lastname}")
logger.info(f"vars {vars(_khoivn)}")
# {'_firstname': 'Khoi', '_lastname': 'VN'}


@dataclass
class UserPrivateAttribute:
    def __init__(self, firstname: str, lastname: str):
        self.__firstname = firstname
        self.__lastname = lastname


__khoivn = UserPrivateAttribute("Khoi", "VN")
assert __khoivn._UserPrivateAttribute__firstname == "Khoi", "No attribute __firstname"
assert __khoivn._UserPrivateAttribute__lastname == "VN", "No attribute __lastname"
logger.info(
    f"UserPrivateAttribute: {__khoivn._UserPrivateAttribute__firstname} \
{__khoivn._UserPrivateAttribute__lastname}"
)  # Khoi VN
logger.info(f"vars {vars(__khoivn)}")
# {'_UserPrivateAttribute__firstname': 'Khoi',
# '_UserPrivateAttribute__lastname': 'VN'}


# --------------------------------------------------
# User attribute collision
# --------------------------------------------------
class UserCollision:
    def __init__(self, firstname: str, lastname: str):
        self.firstname: str = firstname
        self.lastname: str = lastname
        self._age: int = 23
        self._email: str = "nguyenkhoi8071@"
        self.__address: str = "Quang Ngai"
        self.id_: int = 1
        self.type_: str = "admin"
        self.__doc__: str = "This is a user class"
        self.__module__: str = "__main__"
        self.__version__: str = "1.0.0"
        self.__author__: str = "Khoi VN"


khoivn = UserCollision("Khoi", "VN")
logger.info(f"vars {vars(khoivn)}")


def get_public_attributes(obj):
    return {
        attrname: attrvalue
        for attrname in dir(obj)
        if (attrvalue := getattr(khoivn, attrname))
        and not callable(attrvalue)
        and not attrname.startswith("_")
    }


assert get_public_attributes(khoivn) == {
    "firstname": "Khoi",
    "lastname": "VN",
    "id_": 1,
    "type_": "admin",
}
logger.info(get_public_attributes(khoivn))
# {'firstname': 'Khoi', 'id_': 1, 'lastname': 'VN', 'type_': 'admin'}


def get_protected_attributes(obj):
    return {
        attrname: attrvalue
        for attrname in dir(obj)
        if (attrvalue := getattr(obj, attrname))
        and not callable(attrvalue)
        and attrname.startswith("_")
        and not attrname.startswith(f"_{obj.__class__.__name__}_")
        and not attrname.endswith("_")
    }


assert get_protected_attributes(khoivn) == {"_age": 23, "_email": "nguyenkhoi8071@"}
logger.info(get_protected_attributes(khoivn))
# {'_age': 23, '_email': 'nguyenkhoi8071@'}


def get_private_attributes(obj):
    return {
        attrname: attrvalue
        for attrname in dir(obj)
        if (attrvalue := getattr(obj, attrname))
        and not callable(attrvalue)
        and attrname.startswith(f"_{obj.__class__.__name__}_")
    }


assert get_private_attributes(khoivn) == {"_UserCollision__address": "Quang Ngai"}
logger.info(get_private_attributes(khoivn))
# '_UserCollision__address': 'Quang Ngai'


def get_system_attributes(obj):
    return {
        attrname: attrvalue
        for attrname in dir(obj)
        if (attrvalue := getattr(obj, attrname))
        and not callable(attrvalue)
        and attrname.startswith("__")
        and attrname.endswith("__")
    }


assert get_system_attributes(khoivn) == {
    "__author__": "Khoi VN",
    "__dict__": {
        "firstname": "Khoi",
        "lastname": "VN",
        "_age": 23,
        "_email": "nguyenkhoi8071@",
        "_UserCollision__address": "Quang Ngai",
        "id_": 1,
        "type_": "admin",
        "__doc__": "This is a user class",
        "__module__": "__main__",
        "__version__": "1.0.0",
        "__author__": "Khoi VN",
    },
    "__doc__": "This is a user class",
    "__module__": "__main__",
    "__version__": "1.0.0",
}
logger.info(get_system_attributes(khoivn))
