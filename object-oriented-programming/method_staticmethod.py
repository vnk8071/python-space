"""Method Class
- Should not be in a class: method which don't use self in its body
- Should be in class: if method takes self and use it (it requires instances to work)
- If a method don't use self but uses class as a namespace use @staticmethod decorator
- Using class as namespace
- No need to create a class instance
- Will not pass instance (self) as a first method argument

Author: Khoi VN
Date: 15/10/2023
"""

from dataclasses import dataclass
from src.logger import Logger


logger = Logger.get_logger(__name__)


# --------------------------------------------------
# User static method
# --------------------------------------------------
class UserStaticMethod:
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f"UserStaticMethod(self.firstname={self.firstname}, self.lastname={self.lastname})"

    def load_json(self, data):
        import json

        data_json = json.loads(data)
        return UserStaticMethod(**data_json)

    @staticmethod
    def load_json_static_method(data):
        import json

        data_json = json.loads(data)
        return UserStaticMethod(**data_json)


data = '{"firstname": "Khoi", "lastname": "VN"}'
try:
    UserStaticMethod.load_json(data)
except TypeError as e:
    logger.error(e)
    # TypeError: load_json() missing 1 required positional argument: 'data'

try:
    UserStaticMethod().load_json(data)
except TypeError as e:
    logger.error(e)
    # TypeError: UserStaticMethod.__init__() missing 2 required positional arguments: 'firstname' and 'lastname'

UserStaticMethod(None, None).load_json(data)
logger.info(f"UserStaticMethod: {UserStaticMethod(None, None).load_json(data)}")
# UserStaticMethod: UserStaticMethod(self.firstname=Khoi, self.lastname=VN)

UserStaticMethod.load_json_static_method(data)
logger.info(f"UserStaticMethod: {UserStaticMethod.load_json_static_method(data)}")
# UserStaticMethod: UserStaticMethod(self.firstname=Khoi, self.lastname=VN)


# --------------------------------------------------
# User static method dataclass
# --------------------------------------------------


@dataclass
class UserStaticMethodDataclass:
    firstname: str
    lastname: str

    @staticmethod
    def load_json_static_method(data):
        import json

        data_json = json.loads(data)
        return UserStaticMethodDataclass(**data_json)


UserStaticMethodDataclass.load_json_static_method(data)
logger.info(
    f"UserStaticMethodDataclass: {UserStaticMethodDataclass.load_json_static_method(data)}"
)
# UserStaticMethodDataclass: UserStaticMethodDataclass(firstname='Khoi', lastname='VN')
