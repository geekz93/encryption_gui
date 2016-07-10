from tkinter import *
import os
import hashlib

master = Tk()
master.title("hhh")

Password = Entry(master)
Password.grid(row=0, column=0, padx=10, pady=5)


#answer jmpwfzpv
def crack():
    #打开图片
    #通过rename隐藏图片
    enter=Password.get()
    print(enter)
    ans = hashlib.md5(enter.encode("utf8")).hexdigest()
    print(ans)
    if ans == '4b382836be3cd32f7fedc67511c04583':
        hide = "hide.dll"
        letter = "./letter.gif"

        rose = "./rose.exe"
        if hide in os.listdir():
            os.rename("./hide.dll",letter)
        os.system("cmd.exe /c start %s"%letter )
        #延时打开
        os.system("cmd.exe /c start %s"%rose )
    else:#弹出顶层窗口
        pass

OpenButter = Button(master, text="^_^", command=crack ).grid(row=0, column=1)

mainloop()
