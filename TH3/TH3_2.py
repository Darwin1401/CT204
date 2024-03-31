# Ho va Ten: Tran Hai Dang
# MSSV: B2016956
# STT: 13
from sympy import primerange
import random
from math import lcm, gcd

# Thuat toan Euclid mo rong
def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd_extended(b % a, a)
        return (g, x - (b // a) * y, y)
    
def mod_inverse(a, m):
    g, x, y = gcd_extended(a, m)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % m

def generate_key():
    # Chon 2 so nguyen to lon ngau nhien khac nhau
    primes = list(primerange(1000, 2000)) # De tiet kiem thoi gian, co the giam xuong (100, 1000)
    p, q = random.choice(primes), random.choice(primes)
    while(p == q):
        q = random.choice(primes)
    # Tinh n = p * q
    n = p * q
    # Tinh Lambda:
    lambda_n = lcm(p - 1, q - 1)
    # Tim e la so nguyen to dong du voi lambda_n
    for e in range(2, lambda_n):
        if gcd(e, lambda_n) == 1:
            break
    # Tinh d la module nghich dao cua e
    d = mod_inverse(e, lambda_n)
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

def encrypt(plainText, publicKey):
    encoded = []
    for character in plainText:
        encryptedCharacter = ord(character) ** publicKey[1] % publicKey[0]
        encoded.append(encryptedCharacter)
    cipher_txt = "".join([str(i) for i in encoded])
    return encoded, cipher_txt

def decrypt(encoded, privateKey):
    seq = ""
    for num in encoded:
        seq += chr((num ** privateKey[1]) % privateKey[0])
    return seq

if __name__ == "__main__":
    # plainText = input("Nhap chuoi can ma hoa: ")
    plainText = "Hello World"
    # Khoi tao khoa:
    publicKey, privateKey = generate_key()
    # ma hoa:
    encoded, ciphertxt = encrypt(plainText, publicKey)
    deciphertxt = decrypt(encoded, privateKey)

    print("Ma hoa: " + ciphertxt)
    print("Giai ma: " + deciphertxt)