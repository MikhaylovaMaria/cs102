import random
import math
import typing as tp


def is_prime(n: int) -> bool:
    d = 2
    if n == 1:
        return False
    while (d * d <= n) & (n % d != 0):
        d += 1
    return d * d > n   

def gcd(a: int, b: int) -> int:
    
    while a!=0 and b!=0:
        if a > b:
            a%=b
        else:
            b%=a
    d=a+b
    return d    
    

def multiplicative_inverse(e: int, phi: int) -> int:
   
    d = 0
    if phi != 1:
        multiple = 1
        while d == 0:
            if (multiple) % e == 0:
                d = multiple / e
                break
            multiple += phi
    return int(d)   

def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")
    else:
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randrange(1, phi)

        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)
        d = multiplicative_inverse(e, phi)
        return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    
    key, n = pk
    
    cipher = [(ord(char) ** key) % n for char in plaintext]
   
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    
    key, n = pk
   
    plain = [chr((char ** key) % n) for char in ciphertext]
   
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
