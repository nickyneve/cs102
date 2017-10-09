def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    keyword = keyword.lower()
    ciphertext = ''
    n = 0
    for i in plaintext:
        a = ord(keyword[n % len(keyword)]) - ord('a')
        if (ord(i.lower()) - ord('a')) > (26 - a):
            a = a - 26
        ciphertext = ciphertext+chr(ord(i) + a)
        n += 1
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    keyword = keyword.lower()
    plaintext = ''
    n = 0
    for i in ciphertext:
        a = ord(keyword[n % len(keyword)]) - ord('a')
        if (ord(i.lower()) - ord('a')-a) < 0:
            a = a - 26
        plaintext = plaintext + chr(ord(i) - a)
        n += 1
    return plaintext
