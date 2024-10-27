from artcanvas import ArtCanvas
import math
import random
with ArtCanvas() as canvas:
    # Set background
    canvas.fill_background(0.95, 0.95, 0.95)
    # Draw Palestinian flag colors
    heights = [400, 400, 400]
    colors = [(0, 0, 0), (1, 1, 1), (0.0, 0.5, 0)]
    y_pos = 0
    for i in range(3):
        canvas.set_color(*colors[i])
        canvas.draw_rectangle(0, y_pos, 1920, heights[i], True)
        y_pos += heights[i]
    # Draw red triangle
    canvas.set_color(0.8, 0, 0)
    points = [(0, 0), (640, 600), (0, 1200)]
    canvas.draw_polygon(points, True)
    # Add decorative patterns
    canvas.set_color(0.9, 0.9, 0.9, 0.1)
    for i in range(20):
        x = random.randint(700, 1800)
        y = random.randint(100, 1100)
        size = random.randint(30, 100)
        canvas.draw_circle(x, y, size, False)
    # Add crescent moon pattern
    canvas.set_color(0.95, 0.95, 0.95, 0.2)
    for i in range(10):
        x = random.randint(700, 1800)
        y = random.randint(100, 1100)
        radius = random.randint(20, 40)
        canvas.draw_arc(x, y, radius, 0, math.pi * 1.5)
    # Add olive branch motif
    canvas.set_line_width(2)
    canvas.set_color(0.3, 0.5, 0.3, 0.3)
    for i in range(15):
        x = random.randint(700, 1800)
        y = random.randint(100, 1100)
        canvas.draw_bezier_curve(x, y, 
                               x+50, y-20,
                               x+80, y+20,
                               x+100, y)