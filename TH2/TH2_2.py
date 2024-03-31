from Crypto.Cipher import DES
import base64

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

key = "Hello" # can be change at user's will

try:
    with open("TH2\\test.txt") as file:
        # Gan noi dung trong file vao list theo tung dong
        flist = file.readlines()
        # Loai bo ky tu xuong dong
        newlist = []
        for line in flist:
            newlist.append(line.replace("\n", ""))
        # Noi dung goc cua file:
        print("Original content of a file:")
        for line in newlist:
            print(line)
        print()
        # Ma hoa:
        encryptList = []
        for line in newlist:
            encryptList.append(str(mahoa_DES(line, key))[2:-1])
        print("Encrypted content of a file:")
        for line in encryptList:
            print(line)
        print()
        # Giai ma
        decryptList = []
        for line in encryptList:
            decryptList.append(str(giaima_DES(line, key))[2:-1])
        print("Decrypted content of a file: ")
        for line in decryptList:
            print(line)
except FileNotFoundError:
    print("That file was not found :(")