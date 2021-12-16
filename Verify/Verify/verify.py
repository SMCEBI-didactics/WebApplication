import hashlib
import os
import random

"""
"""

def hash_passwd(passwd, n=32):
    """Function that creates hash from given password and random salt.

    Args:
        passwd (str): The password chosen by user.
        n (int, optional): The range of salt. Defaults to 32.

    Returns:
        _salt (int): Chosen randomly salt.
        _hash (str): Generated hash.
    """
    _salt = os.urandom(n)
    _hash = hashlib.pbkdf2_hmac("sha256", passwd.encode("utf-8"), _salt, 100000)
    return _salt, _hash

