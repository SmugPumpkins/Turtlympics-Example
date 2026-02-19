# swap_y_axis

| Input                  | Process              | Output             |
| ---------------------- | -------------------- | ------------------ |
| `x`: Initial x value | Multiply `y` by -1 | `x`: New x value |
| `y`: Initial y value |                      | `y`: New y value |

# scale_point

| Input                      | Process                                                    | Output                        |
| -------------------------- | ---------------------------------------------------------- | ----------------------------- |
| `x`: The initial x value | Create `scaled_x` equal to `x` multiplied by a scalar. | `scaled_x`: The new x value |
| `y`: The initial y value | Create `scaled_y` equal to `y` multiplied by a scalar. | `scaled_y`: The new y value |

# translate_point

| Input                      | Process                                               | Output                            |
| -------------------------- | ----------------------------------------------------- | --------------------------------- |
| `x`: The initial x value | Create `translated_x` equal to `x` plus an offset | `translated_x`: The new x value |
| `y`: The initial y value | Create `translated_y` equal to `y` plus an offset | `translated_y`: The new y value |

# create_turtle

| Input                                                | Process                                       | Output                                       |
| ---------------------------------------------------- | --------------------------------------------- | -------------------------------------------- |
| `shape`: A string representing the turtle's shape. | Create `new_turtle`                         | `new_turtle`: The turtle that was created. |
| `color`: A string representing the turtle's color. | Set the shape of `new_turtle` to `shape`  |                                              |
|                                                      | Setthe  color of `new_turtle` to `color` |                                              |

# line

| Input                                         | Process                                               | Output                                                               |
| --------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------- |
| `x1`: The x value for start of the line     | Scale `x1` and `y1`                               | Render a line with coordinates (`x1`, `y1`) and (`x2`, `y2`) |
| `y1`: The y value for the start of the line | Translate `x1` and `y1`                           |                                                                      |
| `x2`: The x value for the end of the line  | Swap the y axis of `x1` and `y1`                  |                                                                      |
| `y2`: The y value for the end of the line   | Scale `x2` and `y2`                               |                                                                      |
|                                               | Translate `x2` and `y2`                           |                                                                      |
|                                               | Swap the y axis of `x2` and `y2`                  |                                                                      |
|                                               | Draw a line on the canvas with the final coordinates. |                                                                      |

# draw_maze

| Input | Process                               | Output           |
| ----- | ------------------------------------- | ---------------- |
|       | Draw each line from the planned maze. | Render the maze. |

# move_to_start

| Input                                         | Process                                             | Output                                             |
| --------------------------------------------- | --------------------------------------------------- | -------------------------------------------------- |
| `turt`: The turtle to move.                 | Calculate `x`, the pixel coordinate of `cell_x` | Move `turt` to the start position (`x`, `y`) |
| `cell_x`: The starting x cell of the turtle | Calculate `y`, the pixel coordinate of `cell_y` |                                                    |
| `cell_y`: The starting y cell of the turtle | Teleport `turt` to position (`x`, `y`)        |                                                    |

# solve_maze

| Input                                          | Process                                                             | Output                                       |
| ---------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------- |
| `turt`: The turtle to move through the maze. | Use turtle movement commands to navigate `turt` through the maze. | Render `turt` travelling through the maze. |

# main

| Input | Process                         | Output                                  |
| ----- | ------------------------------- | --------------------------------------- |
|       | Draw the maze                   | Render the maze                         |
|       | Create `greg` the turtle      | Render `greg`                         |
|       | Move `greg` to start position | Render `greg` moving through the maze |
|       | Have `greg` solve the maze    |                                         |
