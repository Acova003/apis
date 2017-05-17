import turtle

# opens a window to draw on
window = turtle.Screen()
# makes the window white
window.bgcolor("white")


def draw_square(new_turtle):
    for x in range(0, 4):
        new_turtle.pendown()
        new_turtle.right(90)
        new_turtle.forward(100)


def main():
    # create an instance of Turtle
    # jane = turtle.Turtle()

    # # set values on attributes in the Turtle module
    # jane.shape("turtle")
    # jane.color("green", "yellow")  # outline color, fill color
    # jane.penup()
    # jane.setx(150)

    # # create another instance of Turtle and set its values
    # ginger = turtle.Turtle()
    # ginger.shape("classic")
    # ginger.color("blue")
    # ginger.penup()
    # ginger.setx(-150)

    # # draw one square filled with color with the jane instance
    # jane.begin_fill()
    # draw_square(jane)
    # jane.end_fill()

    # for x in range(0, 1):
    # # draw offset squares in a loop with the ginger instance
    #     draw_square(ginger)
    #     ginger.forward(10)

    # candy_crush = turtle.Turtle()
    # candy_crush.color("black")
    # candy_crush.penup()
    # candy_crush.setx(50)
    
    # for x in range(0, 5):
    #     candy_crush.pendown()
    #     candy_crush.right(144)
    #     candy_crush.forward(50)

    puppy = turtle.Turtle()
    puppy.penup()
    puppy.color("pink", "white")
    puppy.sety(50)

    #puppy face
    puppy.pendown()
    puppy.setx(10)
    puppy.circle(-50)

    #puppy ears
    for x in range(0, 3):
        puppy.pendown()
        puppy.right(120)
        puppy.forward(50)

    puppy.setx(60)
    for x in range(0, 3):
        puppy.pendown()
        puppy.right(120)
        puppy.forward(50)
    



    window.exitonclick()

# The following code will only call the `main` function if we are running *this*
# file from the command line. The main function won't be called if we import
# this file.
# Want to learn more about if __name__ == '__main__':?
# Check out:
# http://stackoverflow.com/a/20158605 and/or
# https://www.youtube.com/watch?v=sugvnHA7ElY
if __name__ == '__main__':
    main()
