# Simple Calculator 1.1
# Created by Sebastian Valverde

# Program config
from tkinter import *
root = Tk()
root.title("Calculator 1.1")

# Gui
info_box = Entry(root, width=33, borderwidth=20, bg="#2C3E50", fg="White")

def fun(number):
    current = info_box.get()
    info_box.delete(0, END)
    info_box.insert(0, str(current) + str(number))
    return

def fun_clear():
    info_box.delete(0, END)
    return


def operation1():
    first_number = info_box.get()
    global f_num
    global op
    f_num = int(first_number)
    op = "addition"
    info_box.delete(0, END)
    return

def operation2():
    first_number = info_box.get()
    global f_num
    global op
    f_num = int(first_number)
    op = "subtraction"
    info_box.delete(0, END)
    return
def operation3():
    first_number = info_box.get()
    global f_num
    global op
    f_num = int(first_number)
    op = "multiplication"
    info_box.delete(0, END)
    return

def operation4():
    first_number = info_box.get()
    global f_num
    global op
    f_num = int(first_number)
    op = "division"
    info_box.delete(0, END)
    return


def fun_equal():
    second_number = info_box.get()
    info_box.delete(0, END)
    if op == "addition":
        info_box.insert(0, f_num + int(second_number))
    elif op == "subtraction":
        info_box.insert(0, f_num - int(second_number))
    elif op == "multiplication":
        info_box.insert(0, f_num * int(second_number))
    elif op == "division":
        info_box.insert(0, f_num / int(second_number))
    else:
        info_box.insert(str("Syntax error"))

    return

# Add buttons
button_1 = Button(root, text="1", padx=40, pady=30, fg="blue", bg="#A3E4D7", command=lambda: fun(1))
button_2 = Button(root, text="2", padx=40, pady=30, fg="blue", bg="#A3E4D7", command=lambda: fun(2))
button_3 = Button(root, text="3", padx=40, pady=30, fg="blue", bg="#A3E4D7", command=lambda: fun(3))
button_4 = Button(root, text="4", padx=40, pady=30, fg="blue", bg="#A3E4D7", command=lambda: fun(4))
button_5 = Button(root, text="5", padx=40, pady=30, fg="blue", bg="#A3E4D7", command=lambda: fun(5))
button_6 = Button(root, text="6", padx=40, pady=30, fg="blue", bg="#A3E4D7", command=lambda: fun(6))
button_7 = Button(root, text="7", padx=40, pady=30, fg="blue", bg="#A3E4D7", command=lambda: fun(7))
button_8 = Button(root, text="8", padx=40, pady=30, fg="blue", bg="#A3E4D7", command=lambda: fun(8))
button_9 = Button(root, text="9", padx=40, pady=30, fg="blue", bg="#A3E4D7", command=lambda: fun(9))
button_0 = Button(root, text="0", padx=40, pady=30, fg="blue", bg="#A3E4D7", command=lambda: fun(0))

# Operations
button_add = Button(root, text="+", padx=25, pady=30, fg="White", bg="#3498DB", command=operation1)
button_sub = Button(root, text="-", padx=25, pady=30, fg="White", bg="#3498DB", command=operation2)
button_mul = Button(root, text="x", padx=25, pady=30, fg="White", bg="#3498DB", command=operation3)
button_div = Button(root, text="/", padx=25, pady=30, fg="White", bg="#3498DB", command=operation4)


button_clear = Button(root, text="C", padx=86, pady=30, fg="red",bg="#58D68D", command=fun_clear)
button_equal = Button(root, text="=",fg="black",bg="#E67E22",padx=20, pady=30, command=fun_equal)



# Buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=2)

button_add.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=4, column=4)



button_clear.grid(row=4, column=0, columnspan=2)
button_equal.grid(row=0, column=4)



info_box.grid( row=0, column=0, columnspan=3,padx=5, pady=10, ipadx=5, ipady=13)


information = Label(root, bg="black", fg="white", text="About the app").grid(row=5, columnspan=5)
information1 = Label(root, bg="black", fg="white", text="Calculator version 1.1").grid(row=6, columnspan=5)
information2 = Label(root, bg="black", fg="white", text="Created by Sebastian Valverde").grid(row=7, columnspan=5)



root.resizable(0, 0)
root.configure(bg="black")
root.mainloop()

# Changelog
# Window is not resizable anymore
# Gui colors
# Buttoms positions
# Buttom colors
# Operations Added





