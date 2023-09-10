import turtle as t
import random

colors_list = [(20, 16, 11), (101, 96, 86), (234, 229, 218), (166, 160, 149), (20, 15, 18), (6, 8, 6), (9, 9, 13),
               (98, 92, 95), (162, 155, 158), (234, 228, 230), (137, 133, 108), (201, 197, 171), (71, 68, 48),
               (92, 92, 96), (91, 95, 91), (153, 153, 157), (154, 157, 154), (228, 231, 228), (135, 125, 122),
               (223, 223, 227), (199, 188, 185), (70, 61, 58), (69, 60, 64), (132, 124, 127), (196, 188, 192),
               (62, 61, 68), (127, 125, 132), (61, 66, 59), (125, 129, 124), (189, 189, 197), (189, 194, 187)]

screen = t.Screen()
screen.setup(800, 600)
screen.title("Recreation of Rabbit Hole by Jackson Pollock")

t.colormode(255)
pollock = t.Turtle()
pollock.speed(0)

num_circles = 100  # Number of concentric circles (You can adjust this to get the canvas filled up)
circle_radius = 10  # Radius of the first circle  (You can adjust this to start with a smaller or bigger circle)


for _ in range(num_circles):
    pollock.penup()
    pollock.goto(0, -circle_radius)  # Start below the center
    pollock.pendown()

    # Choose a random color for the circle
    circle_color = random.choice(colors_list)
    pollock.pencolor(circle_color)

    pollock.circle(circle_radius)

    # Add random dots
    for _ in range(random.randint(2, 10)):  # Adjust the range for the number of dots
        x = random.randint(-circle_radius, circle_radius)
        y = random.randint(-circle_radius, circle_radius)
        pollock.penup()
        pollock.goto(x, y)

        # Choose a random color for the dot
        dot_color = random.choice(colors_list)
        pollock.dot(random.randint(1, 5), dot_color)

    circle_radius += random.randint(10, 30)  # Change spacing to a random number

screen.exitonclick()








