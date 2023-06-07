import turtle

window = turtle.Screen()
window.bgcolor("#DCCAFF")
window.title("Feliz dia dos namorados!")

pen = turtle.Turtle()
pen.color("#E10043")
pen.fillcolor("#E10043")
pen.pensize(3)
pen.speed(7)

pen.begin_fill()
pen.left(140)
pen.forward(224)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.left(120)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.forward(224)
pen.end_fill()

pen.up()
pen.goto(0, -70)
pen.down()
pen.color("#7A003E")
pen.write("Feliz dia dos namorados meu amor, eu te amo!",
          align="center", font=("Century Gothic", 16, "bold"))

pen.hideturtle()

turtle.done()