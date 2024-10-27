from artcanvas import ArtCanvas
import math
import random
with ArtCanvas() as canvas:
    # Fill background with light blue
    canvas.fill_background(0.9, 0.95, 1.0)
    # Draw intricate mandala pattern
    center_x = 960
    center_y = 600
    # Create multiple circular patterns
    for radius in range(50, 551, 50):
        petals = int(radius / 25) * 2
        for i in range(petals):
            angle = (2 * math.pi * i) / petals
            x1 = center_x + radius * math.cos(angle)
            y1 = center_y + radius * math.sin(angle)
            # Draw petal shapes using bezier curves
            canvas.set_color(0.3, 0.4, 0.8, 0.6)
            canvas.set_line_width(2)
            # Control points for bezier curve
            cx1 = x1 + radius/3 * math.cos(angle + math.pi/4)
            cy1 = y1 + radius/3 * math.sin(angle + math.pi/4)
            cx2 = x1 + radius/3 * math.cos(angle - math.pi/4)
            cy2 = y1 + radius/3 * math.sin(angle - math.pi/4)
            canvas.draw_bezier_curve(center_x, center_y, cx1, cy1, cx2, cy2, x1, y1)
        # Add circular details
        canvas.set_color(0.2, 0.3, 0.7, 0.3)
        canvas.draw_circle(center_x, center_y, radius, False)
        # Draw small decorative circles
        for i in range(petals * 2):
            angle = (2 * math.pi * i) / (petals * 2)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            canvas.set_color(0.1, 0.2, 0.6, 0.8)
            canvas.draw_circle(x, y, 5, True)
    # Add center decoration
    canvas.set_color(0.1, 0.2, 0.5, 1.0)
    canvas.draw_circle(center_x, center_y, 30, True)
    # Draw outer decorative border
    canvas.set_color(0.2, 0.3, 0.7, 0.5)
    canvas.set_line_width(10)
    canvas.draw_circle(center_x, center_y, 580, False)