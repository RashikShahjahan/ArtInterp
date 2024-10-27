from artcanvas import ArtCanvas
import math
import random
with ArtCanvas() as canvas:
    # Fill background with dark blue
    canvas.fill_background(0.1, 0.1, 0.2)
    # Create a gradient for the main pattern
    stops = [
        (0, 0.2, 0.5, 0.8, 1),
        (0.5, 0.4, 0.7, 0.9, 0.8),
        (1, 0.6, 0.8, 1, 0.6)
    ]
    canvas.set_gradient(0, 0, 1920, 1200, stops)
    # Draw interconnected circles
    for i in range(12):
        radius = 200 - i * 10
        angle = i * math.pi / 6
        x = 960 + math.cos(angle) * 300
        y = 600 + math.sin(angle) * 300
        canvas.set_line_width(2)
        canvas.draw_circle(x, y, radius, False)
        # Add smaller decorative circles
        for j in range(8):
            inner_angle = j * math.pi / 4
            inner_x = x + math.cos(inner_angle) * (radius/2)
            inner_y = y + math.sin(inner_angle) * (radius/2)
            canvas.draw_circle(inner_x, inner_y, radius/4, False)
    # Add connecting bezier curves
    canvas.set_line_width(1.5)
    for i in range(0, 12, 2):
        angle1 = i * math.pi / 6
        angle2 = ((i + 3) % 12) * math.pi / 6
        x1 = 960 + math.cos(angle1) * 300
        y1 = 600 + math.sin(angle1) * 300
        x2 = 960 + math.cos(angle2) * 300
        y2 = 600 + math.sin(angle2) * 300
        cx1 = (x1 + x2) / 2 + random.randint(-100, 100)
        cy1 = (y1 + y2) / 2 + random.randint(-100, 100)
        cx2 = (x1 + x2) / 2 + random.randint(-100, 100)
        cy2 = (y1 + y2) / 2 + random.randint(-100, 100)
        canvas.draw_bezier_curve(x1, y1, cx1, cy1, cx2, cy2, x2, y2)
    # Add central mandala
    canvas.set_line_width(3)
    for i in range(24):
        angle = i * math.pi / 12
        canvas.move_brush_to(960, 600)
        x = 960 + math.cos(angle) * 150
        y = 600 + math.sin(angle) * 150
        canvas.draw_line_to(x, y)