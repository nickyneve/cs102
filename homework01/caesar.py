def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for i in plaintext:
        if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
            if i == 'x':
                a = 'a'
            elif i == 'y':
                a = 'b'
            elif i == 'z':
                a = 'c'
            elif i == 'X':
                a = 'A'
            elif i == 'Y':
                a = 'B'
            elif i == 'Z':
                a = 'C'
            else:
                a = chr(ord(i) + 3)
            ciphertext = ciphertext + a
        else:
            ciphertext = ciphertext + i
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for i in ciphertext:
        if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
            if i == 'a':
                a = 'x'
            elif i == 'b':
                a = 'y'
            elif i == 'c':
                a = 'z'
            elif i == 'A':
                a = 'X'
            elif i == 'B':
                a = 'Y'
            elif i == 'C':
                a = 'Z'
            else:
                a = chr(ord(i) - 3)
            plaintext = plaintext + a
        else:
            plaintext = plaintext + i
    return plaintext
