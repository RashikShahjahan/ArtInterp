from artcanvas import ArtCanvas
import math
import random
with ArtCanvas() as canvas:
    # Fill background with a deep blue
    canvas.fill_background(0.1, 0.1, 0.2)
    # Create a mandala-like pattern
    center_x, center_y = 960, 600
    # Draw multiple layers of circular patterns
    for radius in range(50, 500, 30):
        num_points = int(radius / 5)
        for i in range(num_points):
            angle = (i * 2 * math.pi) / num_points
            x1 = center_x + radius * math.cos(angle)
            y1 = center_y + radius * math.sin(angle)
            # Set color with slight variations
            hue = (radius + i) / 1000.0
            canvas.set_color(hue, 0.7, 0.9, 0.6)
            # Draw petals using bezier curves
            for j in range(3):
                petal_angle = angle + (j * 2 * math.pi / 3)
                end_x = x1 + 40 * math.cos(petal_angle)
                end_y = y1 + 40 * math.sin(petal_angle)
                ctrl1_x = x1 + 30 * math.cos(petal_angle - 0.5)
                ctrl1_y = y1 + 30 * math.sin(petal_angle - 0.5)
                ctrl2_x = end_x + 30 * math.cos(petal_angle + 0.5)
                ctrl2_y = end_y + 30 * math.sin(petal_angle + 0.5)
                canvas.set_line_width(0.5)
                canvas.draw_bezier_curve(x1, y1, ctrl1_x, ctrl1_y, ctrl2_x, ctrl2_y, end_x, end_y)
    # Add central circles
    for r in range(0, 100, 10):
        canvas.set_color(1, 1, 1, 0.1)
        canvas.set_line_width(2)
        canvas.draw_circle(center_x, center_y, r, False)
    # Add decorative dots around the pattern
    canvas.set_color(1, 1, 1, 0.8)
    for i in range(72):
        angle = (i * 2 * math.pi) / 72
        x = center_x + 520 * math.cos(angle)
        y = center_y + 520 * math.sin(angle)
        canvas.draw_circle(x, y, 3, True)