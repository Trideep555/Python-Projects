from tkinter import  *
from tkinter import messagebox


def resize():
    root.geometry(f"{w.get()}x{h.get()}")
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        exit()

root=Tk()
root.geometry("1000x1000")
root.title("Window Resizer")
Label(root,text="Resize your GUI window",font="lucida 33 bold").grid(row=0,column=3)
while True:
    Label(root,text="Height").grid(row=1,column=1)
    Label(root,text="Width").grid(row=2,column=1)
    h= IntVar()
    w= IntVar()
    Entry(root,textvariable=h).grid(row=1,column=2)
    Entry(root,textvariable=w).grid(row=2,column=2)
    Button(text="Resize",command=resize).grid(row=3,column=2)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()