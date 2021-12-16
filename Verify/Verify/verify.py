import hashlib
import os
import random

"""
This module contains function to 
hash passwords

Examples:
    
    ```
    from Verify import hash_passwd
    passwd = "123"
    _salt, _hash = hash_passwd(passwd)
    print(_salt, _hash)
    ```

"""

def hash_passwd(passwd, n=32):
    """
    Function used to create salt and hash passwords using
    sha256 algorithm.

    Args:
        passwd (str) - password to be hashed
        n (int) - length of salt used to hash password
    
    Returns:
        (_salt, _hash) (string, string) - tuple containing salt and hashed password
    """
    _salt = os.urandom(n)
    _hash = hashlib.pbkdf2_hmac("sha256", passwd.encode("utf-8"), _salt, 100000)
    return _salt, _hash

