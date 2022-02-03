import string
import random
import json


def generate_token() -> str:
    """
    Generates a random token with a length that is > 8 and < 32.
    """
    length = random.randint(8, 32)
    # special characters can cause unintended behavior; could also unpack like [*l1, *l2]
    char_list = string.ascii_letters + string.digits
    rdmtoken = "".join(random.choice(char_list) for i in range(length))
    return f"{rdmtoken}"
