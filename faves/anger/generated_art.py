from artcanvas import ArtCanvas
import math
import random
with ArtCanvas() as canvas:
    # Fill background with dark blue
    canvas.fill_background(0.1, 0.1, 0.2)
    # Center coordinates
    cx, cy = 960, 600
    # Create a radial gradient for the base
    stops = [(0, 0.8, 0.2, 0.6, 1), (0.5, 0.4, 0.1, 0.3, 1), (1, 0.2, 0.05, 0.15, 1)]
    canvas.set_radial_gradient(cx, cy, 0, cx, cy, 400, stops)
    # Draw layers of circles and patterns
    for r in range(50, 401, 50):
        # Draw main circle for each layer
        canvas.draw_circle(cx, cy, r, False)
        # Draw petal patterns
        petals = 12
        for i in range(petals):
            angle = (i * 2 * math.pi) / petals
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            # Draw decorative arcs
            canvas.set_line_width(2)
            canvas.draw_arc(x, y, r/4, angle, angle + math.pi)
            # Add smaller circles at intersections
            canvas.set_color(0.6, 0.2, 0.4, 0.7)
            canvas.draw_circle(x, y, 5, True)
    # Add intricate details with bezier curves
    canvas.set_line_width(1)
    for i in range(24):
        angle = (i * 2 * math.pi) / 24
        x1 = cx + 200 * math.cos(angle)
        y1 = cy + 200 * math.sin(angle)
        x2 = cx + 300 * math.cos(angle + 0.3)
        y2 = cy + 300 * math.sin(angle + 0.3)
        canvas.set_color(0.8, 0.4, 0.6, 0.4)
        canvas.draw_bezier_curve(x1, y1, 
                               x1 + 100, y1 + 100,
                               x2 - 100, y2 - 100,
                               x2, y2)
    # Add central geometric pattern
    canvas.set_color(1, 1, 1, 0.8)
    for i in range(8):
        angle = (i * 2 * math.pi) / 8
        points = []
        for r in [30, 60, 45]:
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            points.append((x, y))
        canvas.draw_polygon(points, False)