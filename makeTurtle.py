import turtle

def createTurtle():
    turtle1 = turtle.Turtle()
    turtle1.color("green")
    turtle1.shape('turtle')
    return turtle1

def create_window(turtle1):
    window = turtle.Screen()
    window.setup(800, 600)
    window.title("Turtle")
    window.exitonclick()
    return window

