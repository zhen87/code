import tkinter
win = tkinter.Tk()
win.title("我是标题")
win.geometry("400x400+200+200")

myFrame = tkinter.Frame(win)#划分一个区域
myFrame.pack()
#left
frm_l = tkinter.Frame(myFrame)
label1 = tkinter.Label(frm_l,text="左上",bg="red")
label1.pack(side=tkinter.TOP)
label2 = tkinter.Label(frm_l,text="左上",bg="blue")
label2.pack(side=tkinter.TOP)
frm_l.pack(side=tkinter.LEFT)

frm_2 = tkinter.Frame(myFrame)
label1 = tkinter.Label(frm_2,text="右1",bg="green")
label1.pack(side=tkinter.TOP)
label2 = tkinter.Label(frm_2,text="右2",bg="pink")
label2.pack(side=tkinter.TOP)
frm_2.pack(side=tkinter.RIGHT)
win.mainloop()