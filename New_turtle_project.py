import turtle as t
import random


def game_starter(member_count):
    dx = t.Turtle()
    dx.speed(15)
    x = 300
    y = 230
    for times in range(member_count):
        dx.penup()
        dx.goto(x, y)
        dx.pendown()
        dx.circle(50)
        y -= 110
    dx.hideturtle()


class new_turtle(t.Turtle):
    siralama = 0
    x = -350
    y = 280

    def __init__(self, ncolor):
        super().__init__("turtle")
        self.name = ncolor
        self.color(ncolor)
        self.speed(2)
        self.totaldistance = 0
        self.shapesize(3)
        self.penup()
        self.goto(new_turtle.x, new_turtle.y)
        self.pendown()
        new_turtle.y -= 110

    def draw(self):
        dtnc = random.randint(50, 150)
        self.fd(dtnc)
        self.totaldistance += dtnc


game_starter(6)

a = new_turtle("yellow")
b = new_turtle("black")
c = new_turtle("red")
d = new_turtle("blue")
e = new_turtle("purple")
f = new_turtle("green")
new_set = {a, b, c, d, e, f}
while True:
    for member in new_set:
        member.draw()
        if member.totaldistance >= 626:
            print(f"{new_turtle.siralama + 1}. {member.name}")
            new_turtle.siralama += 1
    if a.totaldistance >= 626:
        a.hideturtle()
        a.penup()
        new_set.discard(a)
    if b.totaldistance >= 626:
        b.hideturtle()
        b.penup()
        new_set.discard(b)
    if c.totaldistance >= 626:
        c.hideturtle()
        c.penup()
        new_set.discard(c)
    if d.totaldistance >= 626:
        d.hideturtle()
        d.penup()
        new_set.discard(d)
    if e.totaldistance >= 626:
        e.hideturtle()
        e.penup()
        new_set.discard(e)
    if f.totaldistance >= 626:
        f.hideturtle()
        f.penup()
        new_set.discard(f)

    if len(new_set) == 0:
        break