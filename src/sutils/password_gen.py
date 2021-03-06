from random import choice
from string import (
    ascii_lowercase,
    ascii_uppercase,
    punctuation,
    digits
)
from hashlib import sha256
from time import sleep


def password_gen() -> None:
    """Generate 32 char password and print the hash for shell capture."""

    str_set: list[str] = [
            ascii_lowercase,
            ascii_uppercase,
            punctuation,
            digits
        ]
    password: str = "".join([choice(choice(str_set)) for x in range(32)])

    print(password, end="\r")
    sleep(10)
    print(sha256(password.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    password_gen()
