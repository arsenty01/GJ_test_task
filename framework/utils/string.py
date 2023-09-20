"""
    some strings utilities
"""
import string
from random import choice


def get_random_string(length: int = 8) -> str:
    return ''.join(choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(length))


def get_fake_captcha() -> str:
    return ''.join(choice(string.ascii_lowercase + string.digits) for _ in range(6))

