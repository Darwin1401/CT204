# Ho va ten: Tran Hai Dang
# MSSV: B2016956
# STT: 13

from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from tkinter import *

def hashing():
    content = plaintxt.get().encode()
    func = hashmode.get()

    if func == 0:
        result = MD5.new(content)
    elif func == 1:
        result = SHA1.new(content)
    elif func == 2:
        result = SHA256.new(content)
    else:
        result = SHA512.new(content)

    rs = result.hexdigest().upper()
    hashvalue.delete(0, END)
    hashvalue.insert(INSERT, rs)

# Khoi tao man hinh chinh:
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

# Them cac control
lb0 = Label(window, text = " ", font = ("Arial Bold", 10))
lb0.grid(column = 0, row = 0)
lb1 = Label(window, text = "CHƯƠNG TRÌNH BĂM", font = ("Arial Bold", 20))
lb1.grid(column = 1, row = 1)
plainlb2 = Label(window, text = "Văn bản", font = ("Arial", 14))
plainlb2.grid(column = 0, row = 2)
plaintxt = Entry(window, width = 90)
plaintxt.grid(column = 1, row = 2)
hashlb3 = Label(window, text = "Giá trị băm", font = ("Arial", 14))
hashlb3.grid(column = 0, row = 8)
hashvalue = Entry(window, width = 90)
hashvalue.grid(column = 1, row = 8)

# Tao cac radio
radioGroup = LabelFrame(window, text = "Hàm băm")
radioGroup.grid(column = 1, row = 3)
hashmode = IntVar()
hashmode.set(-1)

md5_func = Radiobutton(radioGroup,
                       text = "Hash MD5",
                       font = ("Times New Roman", 11),
                       variable = hashmode,
                       value = 0,
                       command = hashing)
md5_func.grid(column = 0, row = 4)

sha1_func = Radiobutton(radioGroup,
                        text = "Hash SHA1",
                        font = ("Times New Roman", 11),
                        variable = hashmode,
                        value = 1,
                        command = hashing)
sha1_func.grid(column = 0, row = 5)

sha256_func = Radiobutton(radioGroup,
                          text = "Hash SHA256",
                          font = ("Times New Roman", 11),
                          variable = hashmode,
                          value = 2,
                          command = hashing)
sha256_func.grid(column = 0, row = 6)

sha512_func = Radiobutton(radioGroup,
                          text = "Hash SHA512",
                          font = ("Times New Roman", 11),
                          variable = hashmode,
                          value = 3,
                          command = hashing)
sha512_func.grid(column = 0, row = 7)

# Hien thi cua so
window.geometry("800x600")
window.mainloop()