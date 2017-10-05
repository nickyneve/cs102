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
        if i in shift_plus_3:
            ciphertext = ciphertext + shift_plus_3[i]
        else:
            ciphertext = ciphertext + chr(ord(i)+3)
    return ciphertext

shift_plus_3 = {
    'x': 'a',
    'y': 'b',
    'z': 'c',
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}


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
        if i in shift_minus_3:
            plaintext = plaintext + shift_minus_3[i]
        else:
            plaintext = plaintext + chr(ord(i) - 3)
    return plaintext


shift_minus_3 = {
    'x': 'a',
    'y': 'b',
    'z': 'c',
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

print(encrypt_caesar("python"))
print(encrypt_caesar("marina"))
print(decrypt_caesar("pdulqd"))