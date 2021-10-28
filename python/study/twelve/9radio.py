import tkinter
win = tkinter.Tk()
win.title("我是标题")
win.geometry("400x400+200+200")
def go():
    print(r.get())
#绑定一下变量
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win,text="one",value="10",variable=r,command=go)
radio1.pack()
radio2 = tkinter.Radiobutton(win,text="two",value="20",variable=r,command=go)
radio2.pack()
radio3 = tkinter.Radiobutton(win,text="three",value="30",variable=r,command=go)
radio3.pack()
win.mainloop()




