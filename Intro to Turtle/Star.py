import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("Lightblue")
screen.title("Shapes")

board = turtle.Turtle()
board.speed(2)
board.color("Black")

for i in range(5):
    board.forward(100)
    board.right(144)

turtle.done()