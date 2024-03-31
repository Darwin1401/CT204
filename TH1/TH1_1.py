# Họ và tên: Trần Hải Đăng
# MSSV: B2016956
# STT: 13

def Char2Num(c):
    temp = 0
    if ord(c) >= 65 and ord(c) <= 90:
        temp = 65
    elif ord(c) >= 97 and ord(c) <= 122:
        temp = 97
    return ord(c) - temp, temp

def Num2Char(n, temp):
    return chr(n + temp)

# Function to encrypt a text using Affine cipher
# Input:
# txt (string): a string that needs to be encrypt
# a (int): first key
# b (int): second key
# m (int): size of the alphabet
# Output:
# r (string): a string after encryption
def encryptAF(txt, a, b, m = 26):
    r = ""
    for c in txt:
        if c == " ":
            r += c
        else:
            num, temp = Char2Num(c)
            e = (a * num + b) % m
            r += Num2Char(e, temp)
    return r

print(encryptAF("HELLO", 3, 5))