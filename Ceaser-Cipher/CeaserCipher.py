import string
from typing import Dict


def generateKey(n : int) -> Dict[str,str]:
    """generate a key for ceaser cipher

    Parameters
    ----------
    n : int
        amount of charectors to skip

    Returns
    -------
    Dict[str,str]
        A dictionary cipher key
    """
    letters = string.ascii_uppercase
    
    key = {letters[i]: letters[(i + n) % 26] for i in range(len(letters))}

    return key

def encrypt(key, msg):
    """encrypt a message using a key

    Parameters
    ----------
    key : Dict[str,str]
        A dictionary cipher key
    msg : str
        A message to encrypt

    Returns
    -------
    str
        A encrypted message
    """
    
    converted = [key[c] if c in key else c for c in msg]
    return ''.join(converted)

if __name__ == "__main__":
    key = generateKey(3)
    msg = "Fred is a twat".upper()

    print(f"Unencrpyted: {msg}")
    print(f"Encrypted: {encrypt(key, msg)}")