from tkinter import *
import os
import hashlib
import time

master = Tk()
master.title("hhh")

Password = Entry(master)
Password.grid(row=0, column=0, padx=10, pady=5)
Password.delete(0, END)
Password.insert(0, "请输入密码~")

#answer jmpwfzpv
def crack():
    #弹出顶层窗口
    #设置延时打开exe

    #弹出顶层窗口与sleep冲突
    enter=Password.get()
    print(enter)
    ans = hashlib.md5(enter.encode("utf8")).hexdigest()
    print(ans)

    #flag = False
    
    if ans == 'f7a6d065216090af5ec48c5c7e1332fb':
        #'4b382836be3cd32f7fedc67511c04583':
        #创建顶层窗口
        top = Toplevel()
        top.title("test")
        msg = Label(top, text="testetsttttt").pack()
        #flag = True
        Password.delete(0, END)
        Password.insert(0, "bingo")

        hide = "hide.dll"
        rose = "./rose.exe"

        if hide in os.listdir():
            os.rename("./hide.dll",rose)
             
    else:
        Password.delete(0, END)
        Password.insert(0, "密码不对哦 T_T")

    

OpenButter = Button(master, text="^_^", command=crack ).grid(row=0, column=1)

print("----------")
#曲线救国T_T
print(Password.get())
if "bingo"==Password.get():
    #延时3秒打开
    time.sleep(3)
    os.system("cmd.exe /c start %s"%rose )

mainloop()
