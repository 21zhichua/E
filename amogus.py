import turtle as trtl

def body():
  # Right Leg
  trtl.fillcolor("red")
  trtl.pensize(20)
  trtl.speed(15)
  trtl.begin_fill()
  trtl.right(90)
  trtl.forward(50)
  trtl.right(180)
  trtl.circle(40, -180)
  # Head
  trtl.right(180)
  trtl.forward(200)
  trtl.right(180)
  trtl.circle(100, -180)
  # Left Leg
  trtl.backward(20)
  trtl.left(15)
  trtl.circle(500, -20)
  trtl.backward(20)
  trtl.circle(40, -180)
  trtl.left(7)
  trtl.backward(50)
  # Leg Gap
  trtl.up()
  trtl.left(90)
  trtl.forward(10)
  trtl.right(90)
  trtl.down()
  trtl.right(240)
  trtl.circle(50, -70)
  trtl.end_fill()
def visor():
  # Reposition
  trtl.penup()
  trtl.right(230)
  trtl.forward(100)
  trtl.left(90)
  trtl.forward(20)
  trtl.right(90)
  trtl.pendown()
  trtl.fillcolor("cyan")
  trtl.begin_fill()
  trtl.right(150)
  trtl.circle(90, -55)
  trtl.right(180)
  trtl.forward(1)
  trtl.right(180)
  trtl.circle(10, -65)
  trtl.right(180)
  trtl.forward(110)
  trtl.right(180)
  trtl.circle(50, -190)
  trtl.right(170)
  trtl.forward(80)
  trtl.right(180)
  trtl.circle(45, -30)
  trtl.end_fill()

def backpack():
  trtl.penup()
  trtl.goto(-90,0)
  trtl.pendown()
  trtl.fillcolor("red") 
  trtl.begin_fill() 
  trtl.right(155)
  trtl.forward(40)

  for i in range(9):
    trtl.right(10)
    trtl.forward(5)

  trtl.forward(100)

  for i in range(9):
    trtl.right(10)
    trtl.forward(5)
  trtl.forward(30)
  trtl.end_fill()

body()
visor()
backpack()
print("Sussy Baka")
wn = trtl.Screen()
wn.mainloop()