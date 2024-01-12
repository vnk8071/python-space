"""Property Decorator
- Disable attribute modification
- Logging value access

Author: Khoi VN
Date: 15/10/2023
"""

from src.logger import Logger


logger = Logger.get_logger(__name__)


class UserProperty:
    def __init__(self, firstname: str, lastname: str):
        self._firstname = firstname
        self._lastname = lastname

    @property
    def fullname(self):
        return f"{self._firstname} {self._lastname}"

    @fullname.setter
    def fullname(self, fullname: str):
        self._firstname, self._lastname = fullname.split(" ")

    @fullname.deleter
    def fullname(self):
        self._firstname, self._lastname = None, None


user_property = UserProperty("Khoi", "VN")
assert user_property._firstname == "Khoi"
assert user_property._lastname == "VN"
logger.info(f"UserProperty: {user_property._firstname} - {user_property._lastname}")
# UserProperty: Khoi - VN
assert user_property.fullname == "Khoi VN"
logger.info(f"UserProperty: {user_property.fullname}")
# UserProperty: Khoi VN

user_property.fullname = "Kelvin VN"
assert user_property._firstname == "Kelvin"
assert user_property._lastname == "VN"
logger.info(f"UserProperty: {user_property._firstname} - {user_property._lastname}")
# UserProperty: Kelvin - VN
assert user_property.fullname == "Kelvin VN"
logger.info(f"UserProperty: {user_property.fullname}")
# UserProperty: Kelvin VN

del user_property.fullname
assert user_property._firstname is None
assert user_property._lastname is None
logger.info(f"UserProperty: {user_property._firstname} - {user_property._lastname}")
# UserProperty: None - None
