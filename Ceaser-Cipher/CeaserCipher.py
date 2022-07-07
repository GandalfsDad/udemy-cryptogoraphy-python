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

def encrypt(key : Dict[str, str], msg : str) -> str:
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

def decrypt(key : Dict[str, str], msg : str) -> str:
    """decrypt a message using a key

    Parameters
    ----------
    key : Dict[str,str]
        A dictionary cipher key
    msg : str
        A message to decrypt

    Returns
    -------
    str
        A decrypted message
    """
    reverseKey = {v: k for k, v in key.items()}

    return encrypt(reverseKey, msg)


if __name__ == "__main__":
    key = generateKey(3)
    msg = "Fred is a twat".upper()
    encrypted = encrypt(key, msg)
    decrypted = decrypt(key, encrypted)

    print(f"Unencrpyted: {msg}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

    print(f"-"*32)
    print(f"Attempting to break the key")

    for i in range(26):
        key = generateKey(i+1)
        decrypted = decrypt(key, encrypted)

        print(f"Key {i+1}: {decrypted}")