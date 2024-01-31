""" Class method
- Using class as namespace
- Will pass class as a first argument
- self is not required

Author: Khoi VN
Date: 15/10/2023
"""

import json
from dataclasses import dataclass

from src.logger import Logger

logger = Logger.get_logger(__name__)


class JSONMixinStaticMethod:
    @staticmethod
    def from_json(data):
        data = json.loads(data)
        return UserStaticMethod(**data)


@dataclass
class UserStaticMethod(JSONMixinStaticMethod):
    firstname: str
    lastname: str


data = '{"firstname": "Khoi", "lastname": "VN"}'
logger.info(f"UserClassMethod: {UserStaticMethod.from_json(data)}")
# UserClassMethod: UserClassMethod(firstname='Khoi', lastname='VN')


class JSONMixinClassMethod:
    @classmethod
    def from_json(cls, data):
        data = json.loads(data)
        return cls(**data)


@dataclass
class UserClassMethod(JSONMixinClassMethod):
    firstname: str
    lastname: str


logger.info(f"UserClassMethod: {UserClassMethod.from_json(data)}")
# UserClassMethod: UserClassMethod(firstname='Khoi', lastname='VN')
