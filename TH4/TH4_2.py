# Ho va ten: Tran Hai Dang
# MSSV: B2016956
# STT: 13

from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from tkinter import *
import tkinter.messagebox
import random
import csv
import pandas as pd

def accountGen():
    flag = True
    username = usernametxt.get()
    password = passwordtxt.get()
    if username.find(" ") != -1 or password.find(" ") != -1:
        tkinter.messagebox.showinfo("Error", "Username and Password can't have space(s)!")
        flag = False
    if flag == True:
        cols_name = ["Username", "Hashed Password"]
        df = pd.read_csv("CSDL.csv", names = cols_name, delimiter = "\t", usecols = ["Username"])
        df = df.to_numpy()
        for row in df:
            if username == row[0]:
                tkinter.messagebox.showinfo("Warning", "This user has already been registered!")
                return
        with open("CSDL.csv", "a+", newline = "") as csdl:
            csdl_writer = csv.writer(csdl, delimiter = "\t")
            password = password.encode()
            hash_mode = random.randint(0, 3)
            match hash_mode:
                case 0:
                    password = MD5.new(password)
                    hash_mode = "MD5"
                case 1:
                    password = SHA1.new(password)
                    hash_mode = "SHA1"
                case 2:
                    password = SHA256.new(password)
                    hash_mode = "SHA256"
                case 3:
                    password = SHA512.new(password)
                    hash_mode = "SHA512"
            password = password.hexdigest().upper()
            csdl_writer.writerow([username, password])
            tkinter.messagebox.showinfo("Success", "successful register using " + hash_mode)

# Khoi tao man hinh chinh:
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

# Them cac control
lb0 = Label(window, text = " ", font = ("Arial Bold", 10))
lb0.grid(column = 0, row = 0)
lb1 = Label(window, text = "Tạo tài khoản", font = ("Arial Bold", 20))
lb1.grid(column = 1, row = 1)
usernamelb2 = Label(window, text = "Tên đăng nhập", font = ("Arial", 14))
usernamelb2.grid(column = 0, row = 2)
usernametxt = Entry(window, width = 90)
usernametxt.grid(column = 1, row = 2)
passwordlb3 = Label(window, text = "Mật khẩu", font = ("Arial", 14))
passwordlb3.grid(column = 0, row = 3)
passwordtxt = Entry(window, width = 90, show = "*")
passwordtxt.grid(column = 1, row = 3)

# Tao cac button
accountGenerateBtn = Button(window, text = "Tạo tài khoản", command = accountGen)
accountGenerateBtn.grid(column = 1, row = 4)

# Hien thi cua so
window.geometry("800x600")
window.mainloop()