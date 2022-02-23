from turtle import Turtle


class DashedLine(Turtle):
    def __init__(self):
        super(DashedLine, self).__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.counter = -300
        self.goto(0, -300)
        self.seth(90)

        while self.counter <= 300:
            self.pendown()
            self.fd(20)
            self.counter += 20
            self.penup()
            self.fd(20)
            self.counter += 20


