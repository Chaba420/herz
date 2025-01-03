import turtle
import time

def draw_heart():
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Ein Herz für dich")

    heart = turtle.Turtle()
    heart.speed(3)
    heart.color("red")
    heart.begin_fill()

    heart.left(140)
    heart.forward(223)
    for _ in range(200):
        heart.right(1)
        heart.forward(2)
    heart.left(120)
    for _ in range(200):
        heart.right(1)
        heart.forward(2)
    heart.forward(223)
    heart.end_fill()

    text = turtle.Turtle()
    text.speed(5)
    text.penup()
    text.color("black")
    
    text.goto(0, 200)
    text.write("P+L", align="center", font=("Arial", 24, "bold"))

    text.goto(0, 180)
    text.write("BFF", align="center", font=("Arial", 18, "normal"))

    text.hideturtle()

    time.sleep(20)

    turtle.bye()

if __name__ == "__main__":
    draw_heart()
