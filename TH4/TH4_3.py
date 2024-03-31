# Ho va ten: Tran Hai Dang
# MSSV: B2016956
# STT: 13

from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from tkinter import *
import tkinter.messagebox
import pandas as pd

def login():
    flag = True
    username = usernametxt.get()
    password = passwordtxt.get()
    if username.find(" ") != -1 or password.find(" ") != -1:
        tkinter.messagebox.showinfo("Error", "Username and Password can't have space(s)!")
        flag = False
    if flag == True:
        password = password.encode()
        cols_name = ["Username", "Hashed Password"]
        df = pd.read_csv("CSDL.csv", names = cols_name, delimiter = "\t")
        df = df.to_numpy()
        for row in df:
            flag = False
            if username == row[0]:
                for i in range(0, 4):
                    result = ""
                    match i:
                        case 0:
                            result = MD5.new(password)
                        case 1:
                            result = SHA1.new(password)
                        case 2:
                            result = SHA256.new(password)
                        case 3:
                            result = SHA512.new(password)
                    result = result.hexdigest().upper()
                    if(result == row[1]):
                        tkinter.messagebox.showinfo("Success", "Login successful")
                        flag = True
                        break
                break            
        if not flag:
            tkinter.messagebox.showinfo("Failed", "Failed to login")            
# Khoi tao man hinh chinh:
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

# Them cac control
lb0 = Label(window, text = " ", font = ("Arial Bold", 10))
lb0.grid(column = 0, row = 0)
lb1 = Label(window, text = "Đăng nhập", font = ("Arial Bold", 20))
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
accountGenerateBtn = Button(window, text = "Đăng nhập", command = login)
accountGenerateBtn.grid(column = 1, row = 4)

# Hien thi cua so
window.geometry("800x600")
window.mainloop()