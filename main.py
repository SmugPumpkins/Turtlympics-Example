"""
Turtlympics
Nathan Forsyth
Computer Science 15
STEM Collegiate
"""

import turtle

screen = turtle.Screen()
canvas = screen.getcanvas()
SCALE = 100
CELLS = 6

def swap_y_axis(x : int, y : int):
    """
    Takes a 2D point (x, y) and negates the y value to work with the Turtle window.

    :param x: The x coordinate of (x, y)
    :param y: The y coordinate of (x, y)
    :return: An ordered pair of the new coordinate.
    """
    # print(f"New x: {x}, New y: {-y}")
    return x, -y

def scale_point(x : int, y : int):
    """
    Scales the grid from grid paper coordinates to pixel coordinates.

    :param x: The initial x value
    :param y: The initial y value
    :return: An ordered pair with the scaled up coordinates
    """
    scaled_x, scaled_y = x * SCALE, y * SCALE
    # print(f"Scaled X: {scaled_x}, Scaled Y: {scaled_y}")
    return scaled_x, scaled_y

def translate_point(x : int, y : int):
    """
    Translates points such that the center of the maze will be at the center of the window.

    :param x: The x position to translate.
    :param y: The y position to translate.
    :return: The translated points.
    """
    translate = (CELLS * SCALE) // 2
    # print(f"Translate amount: {translate}")
    # print(f"Translated X: {x - translate}")
    # print(f"Translated Y: {y - translate}")
    return x - translate, y - translate


def create_turtle(shape : str, color : str):
    """
    Generates the turtle with specified shape and color.

    :param shape: The requested shape of the turtle.
    :param color: The requested color of the turtle.
    :return: The generated turtle.
    """
    new_turtle = turtle.Turtle()
    new_turtle.shape(shape)
    new_turtle.color(color)
    return new_turtle

def line(x1, y1, x2, y2):
    """
    Takes an initial pair of coordinates and scales it. Then draws a line on the canvas.

    :param x1: The x position of the first point.
    :param y1: The y position of the first point.
    :param x2: The x position of the second point.
    :param y2: The y position of the second point.
    :return: None
    """
    # print(f"Input Coordinates: {x1}, {y1}, {x2}, {y2}")
    x1, y1 = scale_point(x1, y1)
    x1, y1 = translate_point(x1, y1)
    x1, y1 = swap_y_axis(x1, y1)
    x2, y2 = scale_point(x2, y2)
    x2, y2 = translate_point(x2, y2)
    x2, y2 = swap_y_axis(x2, y2)
    # print(f"Output Coordinates: {x1}, {y1}, {x2}, {y2}")
    canvas.create_line(x1, y1, x2, y2)

def draw_maze():
    """
    Draws the lines of the maze.
    :return: None
    """
    line(0,0,3,0)
    line(4,0,6,0)
    line(3,2,5,2)
    line(0,3,1,3)
    line(2,3,3,3)
    line(1,4,2,4)
    line(3,4,5,4)
    line(2,5,3,5)
    line(0,6,2,6)
    line(3,6,6,6)
    line(0,0,0,6)
    line(1,1,1,3)
    line(1,4,1,6)
    line(2,0,2,3)
    line(3,0,3,1)
    line(3,3,3,5)
    line(4,0,4,3)
    line(4,5,4,6)
    line(5,1,5,2)
    line(5,3,5,5)
    line(6,0,6,6)

def move_to_start(turt : turtle.Turtle, cell_x, cell_y):
    """
    Moves the turtle to the starting cell of the maze.

    :param turt: Turtle to move.
    :param cell_x: The x cell of the start position.
    :param cell_y: The y cell of the start position.
    :return: None
    """
    x = (cell_x * SCALE) - (SCALE // 2)
    y = (cell_y * SCALE) - (SCALE // 2)
    x, y = translate_point(x, y)
    turt.teleport(x, y)

def solve_maze(turt : turtle.Turtle):
    """
    Have the turtle solve the maze.

    :param turt: The turtle to move in the maze.
    :return: None
    """
    turt.lt(90)
    turt.fd(2 * SCALE)
    turt.lt(90)
    turt.fd(SCALE)
    turt.rt(90)
    turt.fd(SCALE)
    turt.rt(90)
    turt.fd(SCALE)
    turt.lt(90)
    turt.fd(SCALE)
    turt.rt(90)
    turt.fd(SCALE)
    turt.rt(90)
    turt.fd(SCALE)
    turt.lt(90)
    turt.fd(SCALE)
    turt.lt(90)
    turt.fd(3 * SCALE)
    turt.lt(90)
    turt.fd(SCALE)
    turt.lt(90)
    turt.fd(SCALE)
    turt.rt(90)
    turt.fd(SCALE)
    turt.rt(90)
    turt.fd(SCALE)
    turt.lt(90)
    turt.fd(SCALE)
    turt.rt(90)
    turt.fd(SCALE)

def main():
    """
    Creates the turtle, turtle maze, and requests input from the user.
    """
    draw_maze()
    greg = create_turtle("turtle", "orange")
    move_to_start(greg, 4, 0)
    solve_maze(greg)
    turtle.done()

if __name__ == "__main__":
    main()