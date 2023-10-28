import turtle

turtle.shape()

def triangle(side):
  turtle.left(240)
  for _ in range(3):
    turtle.forward(side)
    turtle.left(120)

def proton():
  def o():
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
 
  turtle.right(60)
  turtle.forward(150)
  turtle.right(90)
  turtle.forward(80)
  for _ in range(3):
    turtle.right(90)
    turtle.forward(40)
  for _ in range(2):
    turtle.left(90)
    turtle.forward(40)
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(50)
  for _ in range(3):
    turtle.right(90)
    turtle.forward(25)
  turtle.left(135)
  turtle.forward(35)
  turtle.left(45)
  turtle.forward(10)
  o()
  turtle.left(90)
  turtle.forward(50)
  turtle.left(90)
  turtle.backward(15)
  turtle.forward(30)
  turtle.backward(15)
  turtle.left(90)
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(25)
  o()
  turtle.forward(15)
  turtle.backward(30)
  turtle.left(90)
  turtle.forward(50)
  turtle.right(149)
  turtle.forward(59)
  turtle.right(121)
  turtle.forward(70)
  turtle.backward(70)
  turtle.right(90)
  turtle.forward(50)
  turtle.left(990)
  turtle.forward(30)
 

triangle(220)
proton()