import turtle

# t = turtle.Turtle()
# t.speed(0)

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

def draw_square(turtle_obj, size = 100):
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.left(90)

def draw_spiral(t):
    """
    draw one square, turn an angle, then draw another square and so on
    """
    for i in range(36):
        draw_square(t, 50)
        t.left(10)

def main():
    t = turtle.Turtle()
    t.speed(0)
    draw_spiral(t)
    turtle.mainloop()

if __name__ == "__main__":
    main()

