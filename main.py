from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

speed = int(input("Which Level Would You Like? Easy = 3, Medium = 4, Hard = 5: "))
# create screen
screen = Screen()

border_turtle = Turtle()
border_turtle.color("white")
border_turtle.hideturtle()
border_turtle.speed('fastest')
border_turtle.pensize(3)
border_turtle.penup()
border_turtle.goto(-370, 270)  # -370 = -length/2, 270 = height/2
border_turtle.pendown()

# Draw the rectangle (length=740, height=540)
for _ in range(2):
    border_turtle.forward(740)   # Top/bottom sides
    border_turtle.right(90)
    border_turtle.forward(540)   # Left/right sides
    border_turtle.right(90)

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# create paddles, ball, scores
score_l = Score((-200, 275))
score_r = Score((200, 275))
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# draw center dashed line once
divider = Turtle()
divider.color("white")
divider.hideturtle()
divider.penup()
divider.goto(0, 300)
divider.setheading(270)

for _ in range(30):
    divider.pendown()
    divider.forward(10)
    divider.penup()
    divider.forward(10)

# controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


def game():

    ball.reset()

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.01)
        # ball.move()
        ball.fd(speed)
        if abs(ball.ycor()) > 260:
            ball.rebound_sleeping_side()

        # Right paddle collision
        elif 330 < ball.xcor() < 340 and abs(ball.ycor() - r_paddle.ycor()) < 50:
            ball.rebound_standing_side()

        # Left paddle collision
        elif -340 < ball.xcor() < -330 and abs(ball.ycor() - l_paddle.ycor()) < 50:
            ball.rebound_standing_side()

        elif ball.xcor() > 360:
            score_l.increase_score()
            game_is_on = False

        elif ball.xcor() < -360:
            score_r.increase_score()
            game_is_on = False


while score_r.score < 5 and score_l.score < 5:
    time.sleep(1)
    game()


def gameover():
    game_over = Turtle()
    game_over.penup()
    game_over.color("white")
    game_over.goto(0, 0)
    game_over.write("GAME OVER", align="center", font=("Courier", 20, "normal"))


# game over message
if score_r.score > score_l.score :
    score_r.win_statement((180, 0))
    score_l.lose_statement((-180, 0))
    gameover()
else:
    score_r.lose_statement((180, 0))
    score_l.win_statement((-180, 0))
    gameover()


# screen.clear()
# screen.bgcolor("black")
# game_over_text = Score((0, 0))
# game_over_text.write("Game Over", align="center", font=("Courier", 24, "normal"))
screen.exitonclick()
# screen.mainloop()


