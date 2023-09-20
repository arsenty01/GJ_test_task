import attr
from typing import List
from framework.utils.string import get_random_string, get_fake_captcha


@attr.s
class User(object):
    """
        class to describe customer
    """

    email = attr.ib(default=None)
    nickname = attr.ib(default=None)
    password = attr.ib(default=None)
    captcha = attr.ib(default=None)

    def __repr__(self):
        return f'Customer({self.nickname})'


class ObjectFactory(object):
    """
        class that creates some needed objects
    """

    def __init__(self):
        self.instances: List[object] = []

    def create_user_for_login(self, email: str = None, nickname: str = None, password: str = None):
        """
            create demo user just for filling login form
        :param email:
        :param nickname:
        :param password:
        :return:
        """
        user_as_obj = User()
        user_as_obj.email = email or 'pressaa@gaijinent.com'
        user_as_obj.nickname = nickname or get_random_string()
        user_as_obj.password = password or get_random_string()
        user_as_obj.captcha = get_fake_captcha()
        self.instances.append(user_as_obj)
        return user_as_obj




