# Họ và Tên: Trần Hải Đăng
# MSSV: B2016956
# STT: 13

from tkinter import *
from TH1_2 import encryptAF, decryptAF

def mahoa():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    entxt = encryptAF(plaintxt.get(), a, b)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)

def giaima():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    entxt = decryptAF(ciphertxt.get(), a, b)
    deciphertxt.delete(0, END)
    deciphertxt.insert(INSERT, entxt)

# initialize main screen
window = Tk()
window.title("Welcome to Demo AT&BMTT")

# Add more control
lb0 = Label(window, text = " ", font = ("Arial Bold", 10))
lb0.grid(column = 0, row = 0)
lb1 = Label(window, text = "CHƯƠNG TRÌNH DEMO", font = ("Arial Bold", 20))
lb1.grid(column = 1, row = 1)
lb2 = Label(window, text = "MẬT MÃ AFFINE", font = ("Arial Bold", 15))
lb2.grid(column = 0, row = 2)
plainlb3 = Label(window, text = "PLAIN TEXT", font = ("Arial", 14))
plainlb3.grid(column = 0, row = 3)
plaintxt = Entry(window, width = 20)
plaintxt.grid(column = 1, row = 3)
KEYlb4 = Label(window, text = "KEY PAIR", font = ("Arial", 14))
KEYlb4.grid(column = 2, row = 3)
KEYA1 = Entry(window, width = 3)
KEYA1.grid(column = 3, row = 3)
KEYB1 = Entry(window, width = 5)
KEYB1.grid(column = 4, row = 3)
cipherlb5 = Label(window, text = "CIPHER TEXT", font = ("Arial", 14))
cipherlb5.grid(column = 0, row = 4)
ciphertxt = Entry(window, width = 20)
ciphertxt.grid(column = 1, row = 4)
deciphertxt = Entry(window, width = 20)
deciphertxt.grid(column = 3, row = 4)

# Create Buttons
AFbtn = Button(window, text = "Mã Hóa", command = mahoa)
AFbtn.grid(column = 5, row = 3)
DEAFbtn = Button(window, text = "Giải Mã", command = giaima)
DEAFbtn.grid(column = 2, row = 4)

# Display window
window.geometry("800x600")
window.mainloop()