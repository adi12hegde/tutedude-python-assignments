from tkinter import *

window=Tk()
window.title("Tkinter Calculator")
window.geometry('800x500')

e=Entry(window, width=50, borderwidth=5)
e.place(x=250, y=10)

def click(num):
    previous_entered=e.get()
    e.delete(0,END)
    e.insert(0,str(previous_entered)+str(num))

b=Button(window, text='1', width=12, borderwidth=5,command=lambda:click(1))
b.place(x=250,y=50)

b=Button(window, text='2', width=12, borderwidth=5,command=lambda:click(2))
b.place(x=355,y=50)

b=Button(window, text='3', width=12, borderwidth=5,command=lambda:click(3))
b.place(x=460,y=50)

b=Button(window, text='4', width=12, borderwidth=5,command=lambda:click(4))
b.place(x=250,y=90)

b=Button(window, text='5', width=12, borderwidth=5,command=lambda:click(5))
b.place(x=355,y=90)

b=Button(window, text='6', width=12, borderwidth=5,command=lambda:click(6))
b.place(x=460,y=90)

b=Button(window, text='7', width=12, borderwidth=5,command=lambda:click(7))
b.place(x=250,y=130)

b=Button(window, text='8', width=12, borderwidth=5,command=lambda:click(8))
b.place(x=355,y=130)

b=Button(window, text='9', width=12, borderwidth=5,command=lambda:click(9))
b.place(x=460,y=130)

b=Button(window, text='0', width=12, borderwidth=5,command=lambda:click(0))
b.place(x=250,y=170)

def add():
    global math
    global i
    i=int(e.get())
    math='add'
    e.delete(0,END)

def subtract():
    global math
    global i
    i=int(e.get())
    math='sub'
    e.delete(0,END)

def multiply():
    global math
    global i
    i=int(e.get())
    math='mul'
    e.delete(0,END)

def divide():
    global math
    global i
    i=int(e.get())
    math='div'
    e.delete(0,END)

b=Button(window, text='+', width=12, borderwidth=5, command=add)
b.place(x=355,y=170)

b=Button(window, text='-', width=12, borderwidth=5, command=subtract)
b.place(x=460,y=170)

b=Button(window, text='*', width=12, borderwidth=5, command=multiply)
b.place(x=250,y=210)

b=Button(window, text='/', width=12, borderwidth=5, command=divide)
b.place(x=355,y=210)

def equal():
    i2=int(e.get())
    e.delete(0,END)
    if math == 'add':
        e.insert(0,str(i+i2))
    elif math =='sub':
        e.insert(0,str(i-i2))
    elif math =='mul':
        e.insert(0,str(i*i2))
    elif math =='div':
        try:
            e.insert(0,str(i/i2))
        except ZeroDivisionError:
            e.insert(0,'Division by 0 is not possible. Clear and try again')

b=Button(window, text='=', width=12, borderwidth=5, command=equal)
b.place(x=460,y=210)

b=Button(window, text='Clear', width=12, borderwidth=5,command=lambda:e.delete(0,END))
b.place(x=355,y=250)

mainloop()