import tkinter
from tkinter import ttk
win = tkinter.Tk()
win.title("标题")
win.geometry("800x400+300+100")

#表格
tree = ttk.Treeview(win)
tree.pack()

tree["columns"] = ("姓名","年龄","身高","体重")
tree.column("姓名",width=100)
tree.column("年龄",width=100)
tree.column("身高",width=100)
tree.column("体重",width=100)

#设置列的表头
tree.heading("姓名",text="姓名-name")
tree.heading("年龄",text="年龄-name")
tree.heading("身高",text="身高-name")
tree.heading("体重",text="体重-name")

tree.insert("","0",text="line1",values=("张三","28","200","100"))
tree.insert("","1",text="line2",values=("张三","28","200","100"))

win.mainloop()
