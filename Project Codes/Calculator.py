from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()


    elif text == "DEL":
        value=scvalue.get()
        if value == "":
            return None;
        non_digit = ["+", "-", "*", "%", "."]
        for i in range(len(non_digit)):
            if value.count(non_digit[i]):
                x=value.replace(non_digit[i],"")
                scvalue.set(x)
                screen.update()
                return None

        newval=int(value)//10
        if (-10<int(value)<10):
            scvalue.set("")

        else:
            scvalue.set(newval)

        screen.update()




    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("260x560")
root.maxsize(260, 560)
root.minsize(260, 560)
root.title("Calculator By Trideep")
root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X)

buttons = [["C", "%", "DEL", "/"],
           ["7", "8", "9", "*"],
           ["4", "5", "6", "-"],
           ["1", "2", "3", "+"],
           ["00", "0", ".", "="]]


for row in buttons:
    f = Frame(root, bg="black", borderwidth=0)
    f.pack(side=TOP, fill=X)
    for btn in row:
        b = Button(f, text=btn, font=("times new roman", 28, "bold"), relief=FLAT,
                   width=3, height=1, pady=15, bg="black", fg="white",
                   activebackground="black", activeforeground="white")
        b.pack(side=LEFT)
        b.bind("<Button-1>", click)
root.mainloop()
