# Ho va Ten: Tran Hai Dang
# MSSV: B2016956
# STT: 13

from tkinter import *
import tkinter as tk
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import filedialog

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

# s: String
def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def encryptAF(txt, a, b, m) :
    r = ""
    for c in txt:
        if(c == " "):
            r+=c
        else:
            if 'A'<=c and c<='Z':
                temp = ord(c)-65
                e = (a*temp+b) % m
                num2char = chr(e+65)
                r+=num2char
            else:
                temp = ord(c)-97
                e = (a*temp+b) % m
                num2char = chr(e+97)
                r+=num2char
    return r

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m!=0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp+x0
    return x0

def decryptAF(txt,a,b,m):
    r = ""
    a1 = xgcd(a,m)
    for c in txt:
        if(c == " "):
            r +=c
        else:
            if 'A'<=c and c<='Z':
                temp = ord(c)-65
                e = (a1*(temp-b) ) % m
                num2char = chr(e+65)
                r+=num2char
            else:
                temp = ord(c)-97
                e = (a1*(temp-b) ) % m
                num2char = chr(e+97)
                r+=num2char
    return r

def save_file(content, _mode, _title, _filetypes, _defaultextension):
    f = filedialog.asksaveasfile(mode = _mode,
                                 initialdir = "C:\\Users\\trand\\OneDrive\\Desktop\\CT204\\TH5",
                                 title = _title,
                                 filetypes = _filetypes,
                                 defaultextension = _defaultextension)
    if f is None: return
    f.write(content)
    f.close()

def get_key(key_style):
    filename = filedialog.askopenfilename(initialdir = "C:\\Users\\trand\\OneDrive\\Desktop\\CT204\\TH5",
                                          title = "Open " + key_style,
                                          filetypes = (("PEM files", "*.pem"), ("All files", "*.*")))
    if filename is None: return
    file = open(filename, "rb")
    key = file.read()
    file.close()
    return RSA.importKey(key)

class MAHOA_AFFINE(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa Affine")
        self.geometry("800x600")

        self.lb0 = Label(self, text=" ", font = ("Arial Bold", 10))
        self.lb0.grid(column=0, row=0)
        self.lb1 = Label(self, text = "CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
        self.lb1.grid(column=1, row=1)
        self.lb2 = Label(self, text="MẬT MÃ AFFINE", font=("ArialBold", 15))
        self.lb2.grid(column=0, row=2)
        self.plainlb3 = Label(self, text="PLAIN TEXT", font=("Arial", 14))
        self.plainlb3.grid(column=0, row=3)
        self.plaintxt = Entry(self, width=20)
        self.plaintxt.grid(column=1, row=3)
        self.KEYlb4 = Label(self, text="KEY PAIR",font=("Arial", 14))
        self.KEYlb4.grid(column=2, row=3)
        self.KEYA1 = Entry(self,width=3)
        self.KEYA1.grid(column=3, row=3)
        self.KEYB1 = Entry(self,width=5)
        self.KEYB1.grid(column=4, row=3)
        self.ciphertxt3 = Label(self, text="CIPHER TEXT", font=("Arial", 14))
        self.ciphertxt3.grid(column=0, row=4)
        self.KEYC1 = Entry(self,width=20)
        self.KEYC1.grid(column=1, row=4)

        # Tao nut co ten AFbtn
        self.AFbtn = Button(self, text="Mã Hóa", command=self.mahoa)
        self.AFbtn.grid(column=5, row=3)
        self.DFbtn = Button(self, text="Giải Mã", command=self.giaima)
        self.DFbtn.grid(column=2, row=4)
        self.KEYD1 = Entry(self,width=20)
        self.KEYD1.grid(column=3, row=4)
        self.thoat = Button(self, text = "Quay về màn hình chính", command = self.destroy)
        self.thoat.grid(column = 1, row = 5)
    
    def mahoa(self):
        a = int(self.KEYA1.get())
        b = int(self.KEYB1.get())
        m = 26
        entxt = encryptAF(self.plaintxt.get(), a, b, m)
        self.KEYC1.delete(0, END)
        self.KEYC1.insert(INSERT, entxt)
    
    def giaima(self):
        a = int(self.KEYA1.get())
        b = int(self.KEYB1.get())
        m = 26
        entxt = decryptAF(self.KEYC1.get(),a,b,m)
        self.KEYD1.delete(0,END)
        self.KEYD1.insert(INSERT,entxt)

class MAHOA_DES(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa đối xứng")
        self.geometry("800x600")

        self.lb1 = Label(self, text = "CHƯƠNG TRÌNH DEMO", font = ("Arial Bold", 20))
        self.lb1.grid(column = 1, row = 1)
        self.lb2 = Label(self, text = "MẬT MÃ ĐỐI XỨNG DES", font = ("Arial Bold", 15))
        self.lb2.grid(column = 1, row = 2)
        self.plainlb3 = Label(self, text = "Văn bản gốc", font = ("Arial", 14))
        self.plainlb3.grid(column = 0, row = 3)
        self.plaintxt = Entry(self, width = 100)
        self.plaintxt.grid(column = 1, row = 3)
        self.keylb4 = Label(self, text = "Khóa", font = ("Arial", 14))
        self.keylb4.grid(column = 0, row = 4)
        self.keytxt = Entry(self, width = 100)
        self.keytxt.grid(column = 1, row = 4)
        self.cipherlb5 = Label(self, text = "Văn bản được mã hóa", font = ("Arial", 14))
        self.cipherlb5.grid(column = 0, row = 5)
        self.ciphertxt = Entry(self, width = 100)
        self.ciphertxt.grid(column = 1, row = 5)
        self.decipherlb6 = Label(self, text = "Văn bản được giải mã", font = ("Arial", 14))
        self.decipherlb6.grid(column = 0, row = 6)
        self.deciphertxt = Entry(self, width = 100)
        self.deciphertxt.grid(column = 1, row = 6)

        # Them cac button
        self.cipherBtn = Button(self, text = "Mã hóa", command = self.mahoa_DES)
        self.cipherBtn.grid(column = 1, row = 7)
        self.decipherBtn = Button(self, text = "Giải mã", command = self.giaima_DES)
        self.decipherBtn.grid(column = 1, row = 8)
        self.thoat = Button(self, text = "Quay về màn hình chính", command = self.destroy)
        self.thoat.grid(column = 1, row = 9)

    def mahoa_DES(self):
        txt = pad(self.plaintxt.get()).encode("utf8")
        key = pad(self.keytxt.get()).encode("utf8")
        cipher = DES.new(key, DES.MODE_ECB)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0, END)
        self.ciphertxt.insert(INSERT, entxt)

    def giaima_DES(self):
        txt = self.ciphertxt.get()
        txt = base64.b64decode(txt)
        key = pad(self.keytxt.get()).encode("utf8")
        cipher = DES.new(key, DES.MODE_ECB)
        detxt = unpad(cipher.decrypt(txt))
        self.deciphertxt.delete(0, END)
        self.deciphertxt.insert(INSERT, detxt)

class MAHOA_RSA(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa RSA")
        self.geometry("800x600")

        self.lb0 = Label(self, text = " ", font = ("Arial Bold", 10))
        self.lb0.grid(column = 0, row = 0)
        self.lb1 = Label(self, text = "CHƯƠNG TRÌNH DEMO", font = ("Arial Bold", 20))
        self.lb1.grid(column = 1, row = 1)
        self.lb2 = Label(self, text = "MẬT MÃ BẤT ĐỐI XỨNG RSA", font = ("Arial Bold", 15))
        self.lb2.grid(column = 1, row = 2)
        self.originallb3 = Label(self, text = "Văn bản gốc", font = ("Arial", 14))
        self.originallb3.grid(column = 0, row = 3)
        self.originaltxt = Entry(self, width = 90)
        self.originaltxt.grid(column = 1, row = 3)
        self.cipherlb4 = Label(self, text = "Văn bản được mã hóa", font = ("Arial", 14))
        self.cipherlb4.grid(column = 0, row = 4)
        self.ciphertxt = Entry(self, width = 90)
        self.ciphertxt.grid(column = 1, row = 4)
        self.decipherlb5 = Label(self, text = "Văn bản được giải mã", font = ("Arial", 14))
        self.decipherlb5.grid(column = 0, row = 5)
        self.deciphertxt = Entry(self, width = 90)
        self.deciphertxt.grid(column = 1, row = 5)
        self.personalKeylb6 = Label(self, text = "Khóa cá nhân", font = ("Arial", 14))
        self.personalKeylb6.grid(column = 0, row = 6)
        self.personalKeytxt = Text(self, width = 70, height = 10)
        self.personalKeytxt.grid(column = 1, row = 6)
        self.publicKeylb7 = Label(self, text = "Khóa công khai", font = ("Arial", 14))
        self.publicKeylb7.grid(column = 0, row = 7)
        self.publicKeytxt = Text(self, width = 70, height = 10)
        self.publicKeytxt.grid(column = 1, row = 7)

        # Tao cac button
        self.keyGenerateBtn = Button(self, text = "Tạo khóa", command = self.generate_key)
        self.keyGenerateBtn.grid(column = 1, row = 8)
        self.cipherBtn = Button(self, text = "Mã hóa", command = self.mahoa_rsa)
        self.cipherBtn.grid(column = 1, row = 9)
        self.decipherBtn = Button(self, text = "Giải mã", command = self.giaima_rsa)
        self.decipherBtn.grid(column = 1, row = 10)
        self.thoat = Button(self, text = "Quay về màn hình chính", command = self.destroy)
        self.thoat.grid(column = 1, row = 11)

    def generate_key(self):
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
        self.personalKeytxt.delete("1.0", END)
        self.personalKeytxt.insert(END, key.export_key("PEM"))
        self.publicKeytxt.delete("1.0", END)
        self.publicKeytxt.insert(END, key.publickey().export_key("PEM"))

    def mahoa_rsa(self):
        txt = self.originaltxt.get().encode()
        pub_key = get_key("Public key")
        cipher = PKCS1_v1_5.new(pub_key)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0, END)
        self.ciphertxt.insert(INSERT, entxt)

    def giaima_rsa(self):
        txt = self.ciphertxt.get()
        txt = base64.b64decode(txt)
        pri_key = get_key("Private key")
        decipher = PKCS1_v1_5.new(pri_key)
        entxt = decipher.decrypt(txt, "Lỗi khi giải mã RSA").decode()
        self.deciphertxt.delete(0, END)
        self.deciphertxt.insert(INSERT, entxt)

class MainWindow(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self)

        self.mahoa_Affine = Button(text = "Mã hóa Affine", font = ("Times New Roman", 11), command = self.affine)
        self.mahoa_Affine.pack()

        self.mahoa_DES = Button(text = "Mã hóa Des",
                                font = ("Times New Roman", 11),
                                command = self.des)
        self.mahoa_DES.pack()

        self.mahoa_RSA = Button(text = "Mã hóa RSA", font = ("Times New Roman", 11), command = self.rsa)
        self.mahoa_RSA.pack()

        self.thoat = Button(text = "Kết thúc",
                            font = ("Times New Roman", 11),
                            command = quit)
        self.thoat.pack()

    def des(self):
        MAHOA_DES(self)
    
    def affine(self):
        MAHOA_AFFINE(self)
    
    def rsa(self):
        MAHOA_RSA(self)

def main():
    window = tk.Tk()
    window.title("Chương trình chính")
    window.geometry("300x200")
    MainWindow(window)
    window.mainloop()

main()