import turtle as t

col = ['red', 'yellow', 'lime']
t.hideturtle()
t.begin_fill()
t.goto(-60, 150)
t.goto(60, 150)
t.goto(60, -150)
t.goto(-60, -150)
t.goto(-60, 150)
t.end_fill()
t.up()
for i in range(3):
    t.goto(0, 90 - i * 90)
    t.dot(80, col[i])
