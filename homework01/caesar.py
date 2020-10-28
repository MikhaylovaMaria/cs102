import typing as tp
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    if shift == 0:
        ciphertext = plaintext
    else:
        for i in plaintext:
            a = ord(i)
            if a+shift>90 and 65<=a<=90:
                ciphertext += chr(a + shift-26)
            elif a+shift>122 and 97<=a<=122:
                ciphertext += chr(a + shift-26)
            elif (a+shift<=90 and 65<=a<=90) or (a+shift<=122 and 97<=a<=122):
                ciphertext += chr(a + shift)
            else:
                ciphertext += chr(a)
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    if shift == 0:
        plaintext = ciphertext
    else:
        for i in ciphertext:
            a = ord(i)
            if a - shift < 65 and 65 <= a <= 90:
                plaintext += chr(a - shift + 26)
            elif a - shift < 97 and 97 <= a <= 122:
                plaintext += chr(a - shift + 26)
            elif (a - shift >= 65 and 65 <= a <= 90) or (a - shift >= 97 and 97 <= a <= 122):
                plaintext += chr(a - shift)
            else:
                plaintext += chr(a)
    return plaintext
def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift