""" Attribute mutable and immutable
Immutable Types:
- int
- float
- complex
- bool
- None
- str
- bytes
- tuple
- frozenset
- mapping proxy

Mutable Types:
- list
- set
- dict

Author: Khoi VN
Date: 15/10/2023
"""

from typing import List
try:
    import sys
    sys.path.append('.')
    from src.logger import Logger
except ModuleNotFoundError:
    sys.path.append('..')
    from src.logger import Logger


logger = Logger.get_logger(__name__)


# --------------------------------------------------
# User immutable
# --------------------------------------------------
class UserImmutable:
    def __init__(self, firstname: str, lastname: str, groups: List = []):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups


khoivn = UserImmutable('Khoi', 'VN')
kelvin = UserImmutable('Kelvin', 'VN')
logger.info(f"Group of khoivn: {khoivn.groups}")  # []
logger.info(f"Group of kelvin: {kelvin.groups}")  # []

khoivn.groups.append('admin')
khoivn.groups.append('user')
khoivn.groups.append('guest')

# ['admin', 'user', 'guest']
logger.info(f"Group of khoivn: {khoivn.groups} - {hex(id(khoivn))}")
# ['admin', 'user', 'guest']
logger.info(f"Group of kelvin: {kelvin.groups} - {hex(id(kelvin))}")


# --------------------------------------------------
# User mutable
# --------------------------------------------------
class UserMutable:
    def __init__(self, firstname: str, lastname: str, groups: List = None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups or []


khoivn = UserMutable('Khoi', 'VN')
kelvin = UserMutable('Kelvin', 'VN')
logger.info(f"Group of khoivn: {khoivn.groups}")  # []
logger.info(f"Group of kelvin: {kelvin.groups}")  # []

khoivn.groups.append('admin')
khoivn.groups.append('user')
khoivn.groups.append('guest')

# ['admin', 'user', 'guest']
logger.info(f"Group of khoivn: {khoivn.groups} - {hex(id(khoivn))}")
# ['admin', 'user', 'guest']
logger.info(f"Group of kelvin: {kelvin.groups} - {hex(id(kelvin))}")
