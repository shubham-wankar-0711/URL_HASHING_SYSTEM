import random
import string

from url_hashing_app.models import Link
from config.settings import RANDOM_KEY_LENGTH


def get_random_string():
    """Generate a random string of specified length."""
    length = RANDOM_KEY_LENGTH
    letters_and_digits = string.ascii_lowercase + string.digits

    while True:
        key = ''.join(random.choice(letters_and_digits) for i in range(length))

        if not Link.objects.filter(key=key).exists():
            return key
