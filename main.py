
from tkinter import *
from random import *

f = 0
cl = ["blue",'red']

def D():
    global f
    f+=1
    if f == 20:
      canvas.delete("all")
    else:
      pass
    h = randint(1,3)
    if h == 1:
        p = cl[randint(0, 1)]
        B.config()
        a = canvas.create_polygon(randint(0, 500), randint(0, 500), randint(0, 500), randint(0, 500),randint(0, 500),randint(0, 500), fill = p,outline="black")
    elif h == 2:
        p = cl[randint(0, 1)]
        B.config()
        b = canvas.create_rectangle(randint(0, 500),randint(0, 500),randint(0, 500),randint(0, 500),fill = p )
    else:
        p = cl[randint(0, 1)]
        c = canvas.create_oval(randint(0, 500),randint(0, 500),randint(0, 500),randint(0, 500),fill = p)
        B.config()

root=Tk()
root.title('Пр')
root.geometry('500x575')

canvas = Canvas(root, width=500, height=500)
canvas.pack()

A = Button(root, text='Нажать', width=11, height=2, bg='white', command=D)
A.pack()

B = Label(root)
B.pack()

root.mainloop()
