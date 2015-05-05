"""
You are given a set of n rectangles in no particular order.
They have varying widths and heights, but their bottom edges
are collinear, so that they look like buildings on a skyline.
For each rectangle, you’re given the x position of the left edge,
the x position of the right edge, and the height. Your task is
to draw an outline around the set of rectangles so that you can
see what the skyline would look like when silhouetted at night.

e.g.

input: (left, right, height)

[
    (0, 1, 2),
    (2, 4, 5),
    (3, 5, 8),
    (5, 7, 2)
]

output:

[
    (0, 1, 2),
    (2, 3, 5),
    (3, 5, 8),
    (5, 7, 2)
]

reference to :
https://briangordon.github.io/2014/08/the-skyline-problem.html

sol1:
for each rectangle r:
    for each heightmap cell c starting at r.left and ending at r.right:
        c gets the max of r.height and the previous value of c
sol2:
for each critical point c
    c.y gets the height of the tallest rectangle over c


"""
