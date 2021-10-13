from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os



def Newfile():
    global f1
    root.title("Untitled - Texter")
    f1 = None
    Text.delete(1.0, END)


def Openfile():
    global f1
    f1 = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if (f1 == ""):
        f1 = None
    else:
        root.title(os.path.basename(f1) + "-Texter")
        Text.delete(1.0, END)
    f = open(f1, "r")
    Text.insert(1.0, f.read())
    f.close()


def Savefile():
    global f1
    if f1 == None:
        f1 = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                               filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if f1 == "":
            f1 = None
        else:
            f = open(f1, "w")
            f.write(Text.get(1.0, END))
            f.close()
            root.title(os.path.basename(f1) + "-Texter")
    else:
        f = open(f1, "w")
        f.write(Text.get(1.0, END))
        f.close()


def exitapp():
    on_closing()

def cut():
    Text.event_generate("<<Cut>>")


def copy():
    Text.event_generate("<<Copy>>")


def paste():
    Text.event_generate("<<Paste>>")


def about():
    showinfo("About Texter", "Created By Trideep Banerjee By Python Tkinter")


def on_closing():
    global f1
    if f1 == None:
        if askokcancel("Are you sure?", "Do You want to Save file and then quit") == True:
            Savefile()
        else:
            root.destroy()

    else:
        f=open(f1)
        f2=Text.get(1.0, END)
        if f.read().strip() == f2.strip():
            root.destroy()
        else:
            if askokcancel("Are you sure?", "Do You want to Save file and then quit") == True:
                Savefile()
                root.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title("Untitled- Texter")
    root.geometry("644x768")
    root.wm_iconbitmap("notepad.ico")

    Text = Text(root, font="arial 13")
    Text.pack(fill=BOTH, expand=True)
    f1 = None

    menu = Menu(root)
    file = Menu(menu, tearoff=0)
    file.add_command(label="New", command=Newfile)
    file.add_command(label="Open", command=Openfile)
    file.add_command(label="Save", command=Savefile)
    file.add_separator()
    file.add_command(label="Close", command=exitapp)
    menu.add_cascade(label="File", menu=file)

    edit = Menu(menu, tearoff=0)

    edit.add_command(label="Cut", command=cut)
    edit.add_command(label="Copy", command=copy)
    edit.add_command(label="paste", command=paste)
    menu.add_cascade(label="Edit", menu=edit)

    help = Menu(menu, tearoff=0)
    help.add_command(label="About Notes", command=about)
    menu.add_cascade(label="Help", menu=help)

    root.config(menu=menu)
    scroll = Scrollbar(Text)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=Text.yview)
    Text.config(yscrollcommand=scroll.set)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
