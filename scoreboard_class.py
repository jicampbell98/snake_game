from turtle import Screen, Turtle
screen = Screen()
screen.bgcolor("black")

ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    """Keep up the scoreboard for the game"""
    def __init__(self):
        super().__init__()  # This line will make Scoreboard class objects have all of Turtle attributes and methods
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.shape("circle")
        self.shapesize(.1)
        self.goto(-30, 260)
        self.update_score()

    def update_score(self):
        self.clear()  # Clear the previous score
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER. FINAL SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def count_score(self):
        self.score += 1
        self.update_score()

