from tkinter import *
from Crypto.Cipher import DES
import base64

# Them vao cuoi so con thieu cho du boi cua 8
# s: String
def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

# s: String
def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def mahoa_DES():
    txt = pad(plaintxt.get()).encode("utf8")
    key = pad(keytxt.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)

def giaima_DES():
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    key = pad(keytxt.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    deciphertxt.delete(0, END)
    deciphertxt.insert(INSERT, detxt)

# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

# Them cac control
lb0 = Label(window, text = " ", font = ("Arial Bold", 10))
lb0.grid(column = 0, row = 0)
lb1 = Label(window, text = "CHƯƠNG TRÌNH DEMO", font = ("Arial Bold", 20))
lb1.grid(column = 1, row = 1)
lb2 = Label(window, text = "MẬT MÃ ĐỐI XỨNG DES", font = ("Arial Bold", 15))
lb2.grid(column = 1, row = 2)
plainlb3 = Label(window, text = "Văn bản gốc", font = ("Arial", 14))
plainlb3.grid(column = 0, row = 3)
plaintxt = Entry(window, width = 100)
plaintxt.grid(column = 1, row = 3)
keylb4 = Label(window, text = "Khóa", font = ("Arial", 14))
keylb4.grid(column = 0, row = 4)
keytxt = Entry(window, width = 100)
keytxt.grid(column = 1, row = 4)
cipherlb5 = Label(window, text = "Văn bản được mã hóa", font = ("Arial", 14))
cipherlb5.grid(column = 0, row = 5)
ciphertxt = Entry(window, width = 100)
ciphertxt.grid(column = 1, row = 5)
decipherlb6 = Label(window, text = "Văn bản được giải mã", font = ("Arial", 14))
decipherlb6.grid(column = 0, row = 6)
deciphertxt = Entry(window, width = 100)
deciphertxt.grid(column = 1, row = 6)

# Them cac button
cipherBtn = Button(window, text = "Mã hóa", command = mahoa_DES)
cipherBtn.grid(column = 0, row = 7)
decipherBtn = Button(window, text = "Giải mã", command = giaima_DES)
decipherBtn.grid(column = 1, row = 7)

# Hien thi cua so
window.geometry('800x600')
window.mainloop()