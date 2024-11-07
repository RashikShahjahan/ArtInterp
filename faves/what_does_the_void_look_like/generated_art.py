from artcanvas import ArtCanvas
import math
import random
canvas = ArtCanvas()
canvas.fill_background(0.0, 0.0, 0.03)
canvas.set_radial_gradient(960.0, 600.0, 0.0, 960.0, 600.0, 800.0,
    [(0.0, 0.2, 0.0, 0.3, 1.0),
     (0.3, 0.1, 0.0, 0.15, 0.8),
     (0.7, 0.05, 0.0, 0.08, 0.6),
     (1.0, 0.0, 0.0, 0.02, 0.0)])
for i in range(360):
    angle = i * math.pi / 180
    radius = 400.0 + random.uniform(-50.0, 50.0)
    x = 960.0 + math.cos(angle) * radius
    y = 600.0 + math.sin(angle) * radius
    if i == 0:
        canvas.move_brush_to(x, y)
    else:
        canvas.draw_line_to(x, y)
for j in range(20):
    start_angle = random.uniform(0.0, math.pi * 2)
    canvas.set_color(0.1, 0.0, 0.2, 0.3)
    canvas.set_line_width(random.uniform(1.0, 3.0))
    for i in range(30):
        angle = start_angle + (i * 0.2)
        radius = 300.0 + (i * 10) + random.uniform(-20.0, 20.0)
        x = 960.0 + math.cos(angle) * radius
        y = 600.0 + math.sin(angle) * radius
        if i == 0:
            canvas.move_brush_to(x, y)
        else:
            canvas.draw_bezier_curve(
                prev_x, prev_y,
                prev_x + random.uniform(-50.0, 50.0), prev_y + random.uniform(-50.0, 50.0),
                x + random.uniform(-50.0, 50.0), y + random.uniform(-50.0, 50.0),
                x, y
            )
        prev_x, prev_y = x, y
for i in range(200):
    x = random.uniform(460.0, 1460.0)
    y = random.uniform(100.0, 1100.0)
    size = random.uniform(1.0, 4.0)
    opacity = random.uniform(0.1, 0.5)
    canvas.set_color(0.2, 0.0, 0.3, opacity)
    canvas.draw_circle(x, y, size, True)
canvas.save()