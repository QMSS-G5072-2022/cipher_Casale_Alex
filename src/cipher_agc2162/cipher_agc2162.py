def cipher(text, shift, encrypt=True):
    """ Transforms text into an  encrypted string


    Parameters
    ------------
        text: str
            Input string
        shift: int
            Number of characters to offset for encryption
        encrypt:boolean, Optional
            Encryption/decryption flag
    Return
    -----------
        new_text : str
            Transformed input string

    >>> cipher("apple", 1)
    "bqqmf"

    """
    if isinstance(shift, str):
        raise TypeError(f"shift argument is type {type(shift)} ")
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index + 1]
    return new_text