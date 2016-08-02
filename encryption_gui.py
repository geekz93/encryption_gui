from tkinter import *
from encryption_source import *

root = Tk()
#pack(padx, pady) 设置与边框的距离，单位（像素）

class Var:
    msg = ""
    cipher = ""


#初始化拖拽
#sb = Scrollbar(root)
#sb.pack()

#添加文本框，显示文本
#tShowMsg = Text(root, yscrollcommand=sb.set)#文本框注入
#使用pack设置位置
#tShowMsg.pack()
#使用grid()设置位置

txtw = 50
txth = 10
btw = 12
bth = 1#30ppi


tShowMsg = Text(root, width=txtw, height=txth)
tShowMsg.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
#sb.config(command=tShowMsg.yview)


#输入框，只能输入一行
#eInputMsg = Entry(root)
#eInputMsg.pack()
#使用文本框进行输入
eInputMsg = Text( root, width=txtw, height=txth )
eInputMsg.grid( row=2, column=0, rowspan=2, padx=10, pady=10 )

#索引行和列
#def show():
    #删除文本框的内容
#    tShowMsg.delete(1.0, END)#1.0表示第1行0列，END表示最后一行最后一列？
    #tShowMsg.insert(INSERT, eInputMsg.get() )
#    tShowMsg.insert(INSERT, eInputMsg.get(1.0, END))

def encrypt_gui():
    tShowMsg.delete(1.0, END)
    Var.msg = eInputMsg.get(1.0, END)
    Var.cipher = encrypt(Var.msg)
    tShowMsg.insert(INSERT, Var.cipher)

bEncryption = Button( root, text="加密", command=encrypt_gui, width=btw, height=bth)
bEncryption.grid( row=0, column=1, padx=5, pady=10, sticky=N)

def crack_gui():
    tShowMsg.delete(1.0, END)
    Var.cipher = eInputMsg.get(1.0, END)
    Var.msg = crack(Var.cipher)
    tShowMsg.insert(INSERT, Var.msg)

def sav():
    save_info(Var.msg, Var.cipher)
    tShowMsg.delete(1.0, END)
    tShowMsg.insert(INSERT, "保存成功，文件名为record.txt~")

Button(root, text="解密", command=crack_gui, width=btw, height=bth ).place(x=379, y=60)#


Button(root, text="保存", command=sav, width=btw, height=bth).place(x=379, y=110)
#退出
Button(root, text="退出", command=root.quit, width=btw, height=bth).place(x=379, y=160)



mainloop()

