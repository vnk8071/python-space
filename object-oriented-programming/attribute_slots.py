""" Attribute slots
- Faster attribute access
- Space savings in memory (overhead of dict for every object)
- Prevents from adding new attributes
The space savings is from:
- Store value references in slots instead of __dict__
- Denying __dict__ and __weakref__ creation

Author: Khoi VN
Date: 15/10/2023
"""

try:
    import sys
    sys.path.append('.')
    from src.logger import Logger
except ModuleNotFoundError:
    sys.path.append('..')
    from src.logger import Logger


logger = Logger.get_logger(__name__)

# --------------------------------------------------
# User slots
# --------------------------------------------------
class UserSlots:
    __slots__ = ('firstname', 'lastname')

    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname


user = UserSlots('Khoi', 'VN')
assert user.firstname == 'Khoi'
assert user.lastname == 'VN'
logger.info(f"UserSlots: {user.firstname} - {user.lastname}")  # Khoi - VN

try:
    user.age = 23
except AttributeError as e:
    logger.error(e)


class UserSlotsInitArgs:
    __slots__ = ('firstname', 'lastname')

    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


try:
    user_init_args = UserSlotsInitArgs('Khoi', 'VN', 23)
except AttributeError as e:
    logger.error(e)  # 'UserSlotsInitArgs' object has no attribute 'age'


# --------------------------------------------------
# User slots dict
# --------------------------------------------------
class UserSlotsDict:
    __slots__ = ('firstname', 'lastname', '__dict__')

    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


user_dict = UserSlotsDict('Khoi', 'VN', 23)
assert user_dict.firstname == 'Khoi'
assert user_dict.lastname == 'VN'
assert user_dict.age == 23
logger.info(f"UserSlotsDict: {user_dict.firstname} - {user_dict.lastname} - {user_dict.age}")
# UserSlotsDict: Khoi - VN - 23

user_dict.address = 'Quang Ngai'
assert user_dict.address == 'Quang Ngai'
assert user_dict.__dict__ == {'age': 23, 'address': 'Quang Ngai'}
logger.info(user_dict.__dict__)  # {'age': 23, 'address': 'Quang Ngai'}
logger.info(user_dict.__slots__)  # ('firstname', 'lastname', '__dict__')
