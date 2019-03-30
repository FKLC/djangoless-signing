# source: https://github.com/django/django/blob/master/django/utils/crypto.py

"""
Django's standard crypto functions and utilities.
"""
import hashlib
import hmac
import random
import time

from .encoding import force_bytes

# Use the system PRNG if possible
try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    import warnings

    warnings.warn(
        "A secure pseudo-random number generator is not available "
        "on your system. Falling back to Mersenne Twister."
    )
    using_sysrandom = False


def salted_hmac(key_salt, value, secret):
    """
    Return the HMAC-SHA1 of 'value', using a key generated from key_salt and a
    secret (which defaults to settings.SECRET_KEY).

    A different key_salt should be passed in for every application of HMAC.
    """
    key_salt = force_bytes(key_salt)
    secret = force_bytes(secret)

    # We need to generate a derived key from our base key.  We can do this by
    # passing the key_salt and our base key through a pseudo-random function and
    # SHA1 works nicely.
    key = hashlib.sha1(key_salt + secret).digest()

    # If len(key_salt + secret) > sha_constructor().block_size, the above
    # line is redundant and could be replaced by key = key_salt + secret, since
    # the hmac module does the same thing for keys longer than the block size.
    # However, we need to ensure that we *always* do this.
    return hmac.new(key, msg=force_bytes(value), digestmod=hashlib.sha1)


def constant_time_compare(val1, val2):
    """Return True if the two strings are equal, False otherwise."""
    return hmac.compare_digest(force_bytes(val1), force_bytes(val2))
