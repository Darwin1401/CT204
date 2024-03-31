from Crypto.Cipher import DES
import base64
import pandas as pd

# Them vao cuoi so con thieu cho du boi cua 8
# s: String
def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

# s: String
def unpad(s):
    return s[:-ord(s[len(s)-1:])]

# txt(string): noi dung can duoc ma hoa
# key(string): khoa de ma hoa DES
# return: entxt(string): chuoi duoc ma hoa tu txt
def mahoa_DES(txt, key):
    txt = pad(txt).encode("utf8")
    key = pad(key).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    return entxt

# txt(string): noi dung can duoc giai ma
# key(string): khoa de giai ma DES
# return: detxt(string): chuoi duoc giai ma tu txt
def giaima_DES(txt, key):
    txt = base64.b64decode(txt)
    key = pad(key).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    return detxt

# Read content from a url csv
url = "https://raw.githubusercontent.com/umpirsky/country-list/master/data/en/country.csv"
display = ["value"]
df = pd.read_csv(url, usecols = display)
df = df.to_numpy()

plaintxt1 = "The treasure is under the coconut tree"
encryptedtxt1 = "lIZg7tB/NvuG4MXsCDFUsRjvQrjw/UuUGzZw+QMMDF4nGjQCGzY0Uw=="
encryptedtxt2 = "LsmDvf9t1pLPn+NZ99+cVx+V1ROl2/9KNqk9PLTe5uRii/aNc/X3tw=="
encryptedtxt3 = "5cdbWs00vXghkBLECplG8ClNQ2Da5R/9KZ0bAKRs+bPvhwOwIt7Sh2ZZFtxHBAK9"

# finds key:
keys = []
for country in df:
    keys.append(country[0])

true_key = ""
for key in keys:
    decrypted = giaima_DES(encryptedtxt1, key)
    if decrypted == plaintxt1.encode("utf8"):
        true_key = key
        break

print(giaima_DES(encryptedtxt2, true_key))
print(giaima_DES(encryptedtxt3, true_key))