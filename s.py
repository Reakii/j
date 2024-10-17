from tkinter import *
root = Tk()
root.geometry("500x600")
root.title("ok")
def topwin():
    top = Toplevel()
    top.geometry("500x300")
    top.title("ok2")
    L2 = Label(top,text="This is a top level window")
    L2.pack()
    top.mainloop()

L=Label(root,text="Root window")
BTN = Button(root,text="click to open new window",command=topwin)
L.pack()
BTN.pack()
root.mainloop()
