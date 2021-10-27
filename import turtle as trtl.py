import turtle as t
import random as rand
t.fillcolor('orange')
def box():
    t.penup()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(180)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

def fxn(x,y):
  box()
t.onclick(fxn)

wn = t.Screen()
wn.mainloop()
