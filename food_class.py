from turtle import Turtle
import random


class Food(Turtle):  # Here we add Turtle to make sure that the objects inherit the Turtle attributes and methods
    """Manage the food for the snake"""
    def __init__(self):
        super().__init__()  # This line will make Food class objects have all of Turtle attributes and methods
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
