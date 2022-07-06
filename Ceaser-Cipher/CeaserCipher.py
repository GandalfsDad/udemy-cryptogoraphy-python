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



if __name__ == "__main__":
    print(generateKey(3))