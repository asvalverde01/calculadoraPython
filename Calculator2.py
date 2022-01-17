
# Simple Calculator 1.2
# Created by Sebastian Valverde

# Program config
from tkinter import *

root = Tk()
root.title("Calculator 1.2")

# Gui
# Result Box
info_box = Entry(root, width=11, borderwidth=20, bg="#34495E", justify="right", fg="White")

# Last result
last_result = Entry(root, width=10, borderwidth=8, justify="center", bg="grey", fg="black")

l_result = Label(root, font=('Consolas', '15'), bg="orange", text="LAST RESULT: ").grid(row=5, column=0, columnspan=2)

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
    global result

    if op == "addition":
        info_box.insert(0, f_num + int(second_number))
        last_result.delete(0, END)
        result = info_box.get()
        last_result.insert(0, int(result))


    elif op == "subtraction":
        info_box.insert(0, f_num - int(second_number))
        last_result.delete(0, END)
        result = info_box.get()
        last_result.insert(0, int(result))

    elif op == "multiplication":
        info_box.insert(0, f_num * int(second_number))
        last_result.delete(0, END)
        result = info_box.get()
        last_result.insert(0, int(result))


    elif op == "division":
        info_box.insert(0, f_num / int(second_number))
        last_result.delete(0, END)
        result = info_box.get()
        last_result.insert(0, int(result))


    else:
        last_result.insert(str("Syntax error"))
    return


def l_mode():
    root.configure(bg="white")
    button_1.configure(bg="white")
    button_2.configure(bg="white")
    button_3.configure(bg="white")
    button_4.configure(bg="white")
    button_5.configure(bg="white")
    button_6.configure(bg="white")
    button_7.configure(bg="white")
    button_8.configure(bg="white")
    button_9.configure(bg="white")
    button_0.configure(bg="white")
    button_clear.configure(bg="white")
    return


def d_mode():
    root.configure(bg="black")
    button_1.configure(bg="black")
    button_2.configure(bg="black")
    button_3.configure(bg="black")
    button_4.configure(bg="black")
    button_5.configure(bg="black")
    button_6.configure(bg="black")
    button_7.configure(bg="black")
    button_8.configure(bg="black")
    button_9.configure(bg="black")
    button_0.configure(bg="black")
    button_clear.configure(bg="black")
    return

# Add buttons


button_1 = Button(root, font=('Consolas', '20'), borderwidth=7, text="1", padx=25, pady=15, fg="blue", bg="#99A3A4",
                  command=lambda: fun(1))
button_2 = Button(root, font=('Consolas', '20'), borderwidth=7, text="2", padx=25, pady=15, fg="blue", bg="#99A3A4",
                  command=lambda: fun(2))
button_3 = Button(root, font=('Consolas', '20'), borderwidth=7, text="3", padx=25, pady=15, fg="blue", bg="#99A3A4",
                  command=lambda: fun(3))
button_4 = Button(root, font=('Consolas', '20'), borderwidth=7, text="4", padx=25, pady=15, fg="blue", bg="#99A3A4",
                  command=lambda: fun(4))
button_5 = Button(root, font=('Consolas', '20'), borderwidth=7, text="5", padx=25, pady=15, fg="blue", bg="#99A3A4",
                  command=lambda: fun(5))
button_6 = Button(root, font=('Consolas', '20'), borderwidth=7, text="6", padx=25, pady=15, fg="blue", bg="#99A3A4",
                  command=lambda: fun(6))
button_7 = Button(root, font=('Consolas', '20'), borderwidth=7, text="7", padx=25, pady=15, fg="blue", bg="#99A3A4",
                  command=lambda: fun(7))
button_8 = Button(root, font=('Consolas', '20'), borderwidth=7, text="8", padx=25, pady=15, fg="blue", bg="#99A3A4",
                  command=lambda: fun(8))
button_9 = Button(root, font=('Consolas', '20'), borderwidth=7, text="9", padx=25, pady=15, fg="blue", bg="#99A3A4",
                  command=lambda: fun(9))
button_0 = Button(root, font=('Consolas', '20'), borderwidth=7, text="0", padx=25, pady=15, fg="blue", bg="#99A3A4",
                  command=lambda: fun(0))


# Operations
button_add = Button(root, font=('Consolas', '20'), borderwidth=10, text="+", padx=25, pady=15, fg="White", bg="#3498DB",
                    command=operation1)
button_sub = Button(root, font=('Consolas', '20'), borderwidth=10, text="-", padx=25, pady=15, fg="White", bg="#3498DB",
                    command=operation2)
button_mul = Button(root, font=('Consolas', '20'), borderwidth=10, text="x", padx=25, pady=15, fg="White", bg="#3498DB",
                    command=operation3)
button_div = Button(root, font=('Consolas', '20'), borderwidth=10, text="/", padx=25, pady=15, fg="White", bg="#3498DB",
                    command=operation4)

button_clear = Button(root, font=('Consolas', '20'), borderwidth=10, text="C", padx=75, pady=13, fg="red", bg="#5F6A6A",
                      command=fun_clear)
button_equal = Button(root, font=('Consolas', '25'), borderwidth=10, text="=", fg="black", bg="#E67E22", padx=15, pady=15,
                      command=fun_equal)

# Extra buttons
button_quit = Button(root, font=('Consolas', '13'), borderwidth=4, text="QUIT", padx=60, bg="#973DC1",
                     command=root.quit)
button_white = Button(root, font=('Consolas', '13'), borderwidth=2, text="Light mode", comman=l_mode)
button_black = Button(root, font=('Consolas', '13'), borderwidth=2, text="Dark mode", fg="White", bg="black",
                      command=d_mode)

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

button_quit.grid(row=6, column=1, columnspan=3)
button_white.grid(row=6, column=0, columnspan=1)
button_black.grid(row=6, column=3, columnspan=2)

info_box.grid( row=0, column=0, columnspan=3, padx=5, pady=10, ipadx=5, ipady=7)

frame_info = LabelFrame(root, text="About the app:", bg="Grey")


information = Label(frame_info, fg="purple", bg="Grey", text="AlpaCode 2020")\
    .grid(row=6, columnspan=2,)
information1 = Label(frame_info, fg="purple", bg="Grey", text="Calculator version 1.2   Created by Sebastian Valverde")\
    .grid(row=7, columnspan=2)

frame_info.grid(row=9, columnspan=5)
info_box.config(font=("Consolas", 30))
last_result.grid(row=5, column=2, columnspan=3)
last_result.config(font=("Consolas", 15))

root.configure(bg="#212F3D")
root.resizable(0, 0)
root.mainloop()

# Changelog 1.1
# Window is not resizable anymore
# Gui colors
# Buttons positions
# Button colors

# Changelog 1.2
# Operations Added
# App information Updated
# Quit button Added
# Light mode added
# Dark mode added
# Numbers box justified and size upgraded

# Changelog 1.2
# Size of the buttons has been upgraded
