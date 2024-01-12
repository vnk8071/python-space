"""Method Class
- Syntax: staticmethod(function) or @staticmethod, dynamic method, @classmethod

Author: Khoi VN
Date: 15/10/2023
"""

from src.logger import Logger


logger = Logger.get_logger(__name__)


# --------------------------------------------------
# User static method
# --------------------------------------------------
class UserStaticMethod:
    def fullname_static_function(firstname: str, lastname: str):
        return f"{firstname} {lastname}"

    @staticmethod
    def fullname_static_method(firstname: str, lastname: str):
        return f"{firstname} {lastname}"


assert UserStaticMethod.fullname_static_function("Khoi", "VN") == "Khoi VN"
logger.info(
    f"UserStaticMethod: {UserStaticMethod.fullname_static_function('Khoi', 'VN')}"
)
# UserStaticMethod: Khoi VN

assert UserStaticMethod.fullname_static_method("Khoi", "VN") == "Khoi VN"
logger.info(
    f"UserStaticMethod: {UserStaticMethod.fullname_static_method('Khoi', 'VN')}"
)
# UserStaticMethod: Khoi VN

try:
    user_static_method = UserStaticMethod()
    logger.info(
        f"UserStaticMethod: {user_static_method.fullname_static_method('Khoi', 'VN')}"
    )
    # UserStaticMethod: Khoi VN
    logger.info(
        f"UserStaticMethod: {user_static_method.fullname_static_function('Khoi', 'VN')}"
    )
    # TypeError: fullname_static_function() takes 2 positional arguments but 3 were given
except TypeError as e:
    logger.error(e)


# --------------------------------------------------
# User class method
# --------------------------------------------------


class UserClassMethod:
    def fullname_dynamic_method(self, firstname: str, lastname: str):
        return f"{firstname} {lastname}"

    @classmethod
    def fullname_without_class_method(firstname: str, lastname: str):
        return f"{firstname} {lastname}"

    @classmethod
    def fullname_class_method(cls, firstname: str, lastname: str):
        return f"{cls.__name__} {firstname} {lastname}"


user_class_method = UserClassMethod()
assert user_class_method.fullname_dynamic_method("Khoi", "VN") == "Khoi VN"
logger.info(
    f"UserDynamicMethod: {user_class_method.fullname_dynamic_method('Khoi', 'VN')}"
)
# UserDynamicMethod: Khoi VN

try:
    assert user_class_method.fullname_without_class_method("Khoi", "VN") == "Khoi VN"
    logger.info(
        f"UserClassMethod: {UserClassMethod.fullname_without_class_method('Khoi', 'VN')}"
    )
    # TypeError: fullname_without_class_method() takes 2 positional arguments but 3 were given
except TypeError as e:
    logger.error(e)

assert UserClassMethod.fullname_class_method("Khoi", "VN") == "UserClassMethod Khoi VN"
logger.info(f"UserClassMethod: {UserClassMethod.fullname_class_method('Khoi', 'VN')}")
# UserClassMethod: UserClassMethod Khoi VN

try:
    assert (
        UserClassMethod.fullname_class_method("Khoi", "VN") == "UserClassMethod Khoi VN"
    )
    logger.info(
        f"UserClassMethod: {UserClassMethod.fullname_class_method('Khoi', 'VN')}"
    )
    # UserClassMethod: UserClassMethod Khoi VN

    assert UserClassMethod.fullname_dynamic_method("Khoi", "VN") == "Khoi VN"
    logger.info(
        f"UserDynamicMethod: {UserClassMethod.fullname_dynamic_method('Khoi', 'VN')}"
    )
    # TypeError: fullname_dynamic_method() missing 1 required positional argument: 'lastname'
except TypeError as e:
    logger.error(e)
