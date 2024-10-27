from artcanvas import ArtCanvas
import math
import random
with ArtCanvas() as canvas:
    # Background gradient
    canvas.set_gradient(0, 0, 1920, 1200, [
        (0, 0.9, 0.9, 1.0, 1),
        (1, 0.7, 0.7, 0.9, 1)
    ])
    canvas.fill_background(0.9, 0.9, 1.0)
    # Head shape
    canvas.set_color(0.8, 0.7, 0.6)
    canvas.draw_circle(960, 600, 200, True)
    # Hair
    canvas.set_color(0.2, 0.15, 0.1)
    for i in range(40):
        x = 960 + math.cos(i/6) * 200
        y = 500 + math.sin(i/6) * 200
        canvas.draw_bezier_curve(x, y, x+random.randint(-50,50), y-100,
                               x+random.randint(-50,50), y-150,
                               x+random.randint(-70,70), y-200)
    # Eyes
    canvas.set_color(1, 1, 1)
    canvas.draw_circle(900, 550, 30, True)
    canvas.draw_circle(1020, 550, 30, True)
    # Pupils
    canvas.set_color(0.3, 0.5, 0.8)
    canvas.draw_circle(900, 550, 15, True)
    canvas.draw_circle(1020, 550, 15, True)
    # Nose
    canvas.set_color(0.75, 0.65, 0.55)
    canvas.draw_bezier_curve(960, 570, 970, 600, 980, 620, 960, 630)
    # Mouth
    canvas.set_color(0.8, 0.3, 0.3)
    canvas.draw_arc(960, 650, 40, 0, math.pi)
    # Eyebrows
    canvas.set_color(0.2, 0.15, 0.1)
    canvas.set_line_width(5)
    canvas.draw_arc(900, 520, 35, 0.2, math.pi-0.2)
    canvas.draw_arc(1020, 520, 35, 0.2, math.pi-0.2)
    # Neck
    canvas.set_color(0.8, 0.7, 0.6)
    canvas.draw_rectangle(920, 750, 80, 100, True)
    # Shoulders
    canvas.draw_arc(800, 850, 150, 0, math.pi)
    canvas.draw_arc(1120, 850, 150, 0, math.pi)
    # Details
    canvas.set_line_width(2)
    for i in range(10):
        x = 960 + math.cos(i) * 180
        y = 600 + math.sin(i) * 180
        canvas.draw_circle(x, y, 5, False)