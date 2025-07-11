from turtle import Turtle


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.pencolor("white")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align="center", font=("Courier", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def win_statement(self, position):
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.pencolor("white")
        self.write("!!You Win!!", align="center", font=("Courier", 18, "normal"))

    def lose_statement(self, position):
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.pencolor("white")
        self.write("You Lose :(", align="center", font=("Courier", 18, "normal"))
