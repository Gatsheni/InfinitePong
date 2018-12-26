#This is a very simple game of Pong.
#Dubbed Infinite Pong because it can literally go on forever :)
import turtle
import os
#creating the game window
window=turtle.Screen()
window.title("Infinite Pong")
window.bgcolor("blue")
window.setup(width=800, height=600)
window.tracer(0)
#initializing the score variables
score_a = 0
score_b = 0
#creating the first paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)
#creating the second paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)
#creating the ball
ball = turtle.Turtle()
ball.speed(-10)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2
#creating the score board
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0 ",align="center", font=("Verdana", 24, "normal"))
#paddle movement control
def p1_up():
    y=paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def p1_down():
    y=paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def p2_up():
    y=paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def p2_down():
    y=paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

window.listen()
window.onkeypress(p1_up, "w")
window.onkeypress(p1_down, "s")
window.onkeypress(p2_up, "Up")
window.onkeypress(p2_down, "Down")

#Game loop
while True:
    window.update()
    #ball movement control
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
     #if statements setting ball boundery and score keeping if a point is scored 
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        #updating the score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),align="center", font=("Verdana", 24, "normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        #updating the score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),align="center", font=("Verdana", 24, "normal"))
    if ball.xcor()> 340 and (ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() +50 and ball.ycor() > paddle_2.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor()< -340 and (ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() +50 and ball.ycor() > paddle_1.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        
