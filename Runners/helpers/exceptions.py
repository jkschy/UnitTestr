from typing import Optional, Sequence


class NoUserFound(Exception):
    key: str = ""

    def __init__(self, key: str):
        """
        There is no user found with the known ket
        :param key: The failed key
        """
        self.key = key

    def __str__(self):
        return "User: " + self.key + " is not a known user type."

class SessionKeyTaken(Exception):
    key: str = ""

    def __init__(self, key: str):
        """
        There is already an associated session with that key

        Most likely, you need to set a key on a new one since it defaults to "first"
        try adding the key to the :TODO add the location of the key
        :param key:
        """
        self.key = key

    def __str__(self):
        return f"Session with key {self.key} was already taken, try adding a new key"
