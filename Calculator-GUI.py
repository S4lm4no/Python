from tkinter import *


root = Tk()


lbl = Entry(root, width=25, bd=3)

def clearing():
    lbl.delete(0, END)

def showing(num):
    current = lbl.get()
    lbl.delete(0, END)
    lbl.insert(0,str(current) + str(num))

def operation(op):
    global kaka
    kaka = op
    op = int(0)

    first_number = lbl.get()
    global f_num
    f_num = int(first_number)
    lbl.delete(0, END)

def equal():
    if kaka == 1:
        s_num = lbl.get()
        lbl.delete(0, END)
        foo = f_num + int(s_num)
        lbl.insert(0, foo)

    elif kaka == 2:
        s_num = lbl.get()
        lbl.delete(0, END)
        foo = f_num - int(s_num)
        lbl.insert(0, foo)
    elif kaka == 3:
        s_num = lbl.get()
        lbl.delete(0, END)
        foo = f_num * int(s_num)
        lbl.insert(0, foo)
    elif kaka == 4:
        s_num = lbl.get()
        lbl.delete(0, END)
        foo = float(f_num) / float(s_num)
        lbl.insert(0, foo)
        
    


but_7 = Button(root, text='7', bd=5, padx=12, pady=18, command=lambda: showing(7))
but_8 = Button(root, text='8', bd=5, padx=12, pady=18, command=lambda: showing(8))
but_9 = Button(root, text='9', bd=5, padx=12, pady=18, command=lambda: showing(9))

but_4 = Button(root, text='4', bd=5, padx=12, pady=18, command=lambda: showing(4))
but_5 = Button(root, text='5', bd=5, padx=12, pady=18, command=lambda: showing(5))
but_6 = Button(root, text='6', bd=5, padx=12, pady=18, command=lambda: showing(6))

but_1 = Button(root, text='1', bd=5, padx=12, pady=18, command=lambda: showing(1))
but_2 = Button(root, text='2', bd=5, padx=12, pady=18, command=lambda: showing(2))
but_3 = Button(root, text='3', bd=5, padx=12, pady=18, command=lambda: showing(3))

#addition button
add = Button(root, text='+', padx=15, pady=18, bd=9, command=lambda:operation(1))
sub = Button(root, text='-', padx=15, pady=18, bd=9, command=lambda:operation(2))
mul = Button(root, text='x', padx=15, pady=18, bd=9, command=lambda:operation(3))
div = Button(root, text='/', padx=15, pady=18, bd=9, command=lambda:operation(4))


#equal button
equal = Button(root, text='=', padx=15, pady=18, bd=9, command=equal)

#clear 
clear = Button(root, text='Clear', padx=15, pady=18, bd=9, command=clearing)


#griding
lbl.grid(row=0, column=0, columnspan=4)

but_7.grid(row=1, column=0)
but_8.grid(row=1, column=1)
but_9.grid(row=1, column=2)

but_4.grid(row=2, column=0)
but_5.grid(row=2, column=1)
but_6.grid(row=2, column=2)

but_1.grid(row=3, column=0)
but_2.grid(row=3, column=1)
but_3.grid(row=3, column=2)

#operations grid
add.grid(row=1, column=3)
sub.grid(row=2, column=3)
mul.grid(row=3, column=3)
div.grid(row=4, column=3)

#equal grid
equal.grid(row=4, column=2)

#clear grid
clear.grid(row=4, column=0, columnspan=2)

root.mainloop()