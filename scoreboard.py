from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-40, y=270)
        self.write(f'A: {self.score_l}', move=False, align='center', font=('Arial', 20, 'normal'))
        self.goto(x=40, y=270)
        self.write(f'B: {self.score_r}', move=False, align='center', font=('Arial', 20, 'normal'))

    def increase_score_l(self):
        self.clear()
        self.score_l += 1
        self.update_scoreboard()

    def increase_score_r(self):
        self.clear()
        self.score_r += 1
        self.update_scoreboard()

