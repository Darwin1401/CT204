# Ho va ten: Tran Hai Dang
# MSSV: B2016956
# STT: 13

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import *
from tkinter import filedialog

def save_file(content, _mode, _title, _filetypes, _defaultextension):
    f = filedialog.asksaveasfile(mode = _mode,
                                 initialdir = "D:/",
                                 title = _title,
                                 filetypes = _filetypes,
                                 defaultextension = _defaultextension)
    if f is None: return
    f.write(content)
    f.close()

def generate_key():
    key = RSA.generate(1024)
    pri = save_file(key.export_key("PEM"),
                    "wb",
                    "Lưu khóa cá nhân",
                    (("All files", "*.*"), ("PEM files", "*.pem")),
                    ".pem")
    pub = save_file(key.public_key().export_key("PEM"),
                    "wb",
                    "Lưu khóa công khai",
                    (("All files", "*.*"), ("PEM files", "*.pem")),
                    ".pem")
    personalKeytxt.delete("1.0", END)
    personalKeytxt.insert(END, key.export_key("PEM"))
    publicKeytxt.delete("1.0", END)
    publicKeytxt.insert(END, key.publickey().export_key("PEM"))

def get_key(key_style):
    filename = filedialog.askopenfilename(initialdir = "D:/",
                                          title = "Open " + key_style,
                                          filetypes = (("PEM files", "*.pem"), ("All files", "*.*")))
    if filename is None: return
    file = open(filename, "rb")
    key = file.read()
    file.close()
    return RSA.importKey(key)

def mahoa_rsa():
    txt = originaltxt.get().encode()
    pub_key = get_key("Public key")
    cipher = PKCS1_v1_5.new(pub_key)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)

def giaima_rsa():
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    pri_key = get_key("Private key")
    decipher = PKCS1_v1_5.new(pri_key)
    entxt = decipher.decrypt(txt, "Lỗi khi giải mã RSA").decode()
    deciphertxt.delete(0, END)
    deciphertxt.insert(INSERT, entxt)

# Khoi tao man hinh chinh:
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

# Them cac control
lb0 = Label(window, text = " ", font = ("Arial Bold", 10))
lb0.grid(column = 0, row = 0)
lb1 = Label(window, text = "CHƯƠNG TRÌNH DEMO", font = ("Arial Bold", 20))
lb1.grid(column = 1, row = 1)
lb2 = Label(window, text = "MẬT MÃ BẤT ĐỐI XỨNG RSA", font = ("Arial Bold", 15))
lb2.grid(column = 1, row = 2)
originallb3 = Label(window, text = "Văn bản gốc", font = ("Arial", 14))
originallb3.grid(column = 0, row = 3)
originaltxt = Entry(window, width = 90)
originaltxt.grid(column = 1, row = 3)
cipherlb4 = Label(window, text = "Văn bản được mã hóa", font = ("Arial", 14))
cipherlb4.grid(column = 0, row = 4)
ciphertxt = Entry(window, width = 90)
ciphertxt.grid(column = 1, row = 4)
decipherlb5 = Label(window, text = "Văn bản được giải mã", font = ("Arial", 14))
decipherlb5.grid(column = 0, row = 5)
deciphertxt = Entry(window, width = 90)
deciphertxt.grid(column = 1, row = 5)
personalKeylb6 = Label(window, text = "Khóa cá nhân", font = ("Arial", 14))
personalKeylb6.grid(column = 0, row = 6)
personalKeytxt = Text(window, width = 70, height = 10)
personalKeytxt.grid(column = 1, row = 6)
publicKeylb7 = Label(window, text = "Khóa công khai", font = ("Arial", 14))
publicKeylb7.grid(column = 0, row = 7)
publicKeytxt = Text(window, width = 70, height = 10)
publicKeytxt.grid(column = 1, row = 7)

# Tao cac button
keyGenerateBtn = Button(window, text = "Tạo khóa", command = generate_key)
keyGenerateBtn.grid(column = 1, row = 8)
cipherBtn = Button(window, text = "Mã hóa", command = mahoa_rsa)
cipherBtn.grid(column = 1, row = 9)
decipherBtn = Button(window, text = "Giải mã", command = giaima_rsa)
decipherBtn.grid(column = 1, row = 10)

# Hien thi cua so
window.geometry("800x600")
window.mainloop()