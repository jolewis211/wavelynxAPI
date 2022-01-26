import string
import random
import json


def generate_token() -> str:
    """
    Generates a random token with a length that is > 8 and < 32.
    """
    length = random.randint(8, 32)
    rdmtoken = "".join(random.choice(string.printable) for i in range(length))
    return f"{rdmtoken}"
