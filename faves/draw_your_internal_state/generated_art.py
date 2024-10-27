from artcanvas import ArtCanvas
import math
import random
with ArtCanvas() as canvas:
    # Set background
    canvas.fill_background(0.1, 0.1, 0.15)
    center_x, center_y = 960, 600
    # Create multiple circular layers
    for radius in range(50, 501, 50):
        # Vary colors for each layer
        hue = radius / 500
        canvas.set_color(hue, 0.7-hue/2, 0.9, 0.7)
        # Draw petal patterns
        petals = int(radius/25) * 4
        for i in range(petals):
            angle = (i * 2 * math.pi) / petals
            x1 = center_x + radius * math.cos(angle)
            y1 = center_y + radius * math.sin(angle)
            # Create flowing curves between points
            next_angle = ((i + 1) * 2 * math.pi) / petals
            x2 = center_x + radius * math.cos(next_angle)
            y2 = center_y + radius * math.sin(next_angle)
            # Control points for bezier curve
            cx1 = center_x + (radius*1.2) * math.cos(angle + 0.2)
            cy1 = center_y + (radius*1.2) * math.sin(angle + 0.2)
            cx2 = center_x + (radius*1.2) * math.cos(next_angle - 0.2)
            cy2 = center_y + (radius*1.2) * math.sin(next_angle - 0.2)
            canvas.draw_bezier_curve(x1, y1, cx1, cy1, cx2, cy2, x2, y2)
        # Add circular accents
        canvas.set_line_width(2)
        canvas.draw_circle(center_x, center_y, radius, False)
        # Draw small decorative circles
        for i in range(petals):
            angle = (i * 2 * math.pi) / petals
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            canvas.set_color(1-hue, hue, 0.8, 0.5)
            canvas.draw_circle(x, y, 5, True)
    # Add central focal point
    canvas.set_color(0.9, 0.9, 1.0, 1.0)
    canvas.draw_circle(center_x, center_y, 30, True)
    canvas.set_color(0.1, 0.1, 0.15, 1.0)
    canvas.draw_circle(center_x, center_y, 20, True)