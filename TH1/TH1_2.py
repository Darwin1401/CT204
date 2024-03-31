# Họ và Tên: Trần Hải Đăng
# MSSV: B2016956
# STT: 13

from TH1_1 import encryptAF, Char2Num, Num2Char

# Function: Extended Euclidean Algorithm
def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp + x0
    return x0

def decryptAF(txt, a, b, m = 26):
    r = ""
    a1 = xgcd(a, m)
    for c in txt:
        if c == " ":
            r += c
        else:
            num, temp = Char2Num(c)
            e = (a1 * (num - b)) % m
            r += Num2Char(e, temp)
    return r

print(decryptAF(encryptAF("HELLO", 3, 5), 3, 5))