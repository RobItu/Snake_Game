from turtle import Turtle, Screen
screen = Screen()
screen.colormode(255)
with open("data.txt") as file:
    content = file.read()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = int(content)
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color(112, 96, 0)
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write("Score: " + str(self.score) + " High Score: " + str(self.high_score), False, "center", ("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update()
