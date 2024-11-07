from artcanvas import ArtCanvas
import random
with ArtCanvas() as canvas:
    # Background
    canvas.fill_background(0.1, 0.1, 0.15)
    # Define node positions in layers
    layers = [
        [(480, y) for y in range(300, 901, 150)],  # Input layer
        [(960, y) for y in range(200, 1001, 100)],  # Hidden layer
        [(1440, y) for y in range(300, 901, 150)]   # Output layer
    ]
    # Draw connections between nodes
    canvas.set_line_width(0.5)
    for i, layer in enumerate(layers[:-1]):
        for start_node in layer:
            for end_node in layers[i + 1]:
                # Create subtle gradient for connections
                intensity = random.uniform(0.2, 0.4)
                canvas.set_color(0.3, 0.6, 0.9, intensity)
                canvas.move_brush_to(start_node[0], start_node[1])
                canvas.draw_line_to(end_node[0], end_node[1])
    # Draw nodes
    for layer in layers:
        for x, y in layer:
            # Outer glow
            for r in range(30, 0, -5):
                alpha = 0.05 * (1 - r/30)
                canvas.set_color(0.4, 0.7, 1.0, alpha)
                canvas.draw_circle(x, y, r)
            # Core of the node
            canvas.set_color(1.0, 1.0, 1.0, 0.9)
            canvas.draw_circle(x, y, 15, True)
            # Inner detail
            canvas.set_color(0.7, 0.9, 1.0, 0.8)
            canvas.draw_circle(x-5, y-5, 5, True)
    # Add synaptic activity
    for _ in range(50):
        x = random.randint(400, 1500)
        y = random.randint(200, 1000)
        canvas.set_color(0.4, 0.8, 1.0, 0.3)
        radius = random.uniform(5, 20)
        for i in range(5):
            canvas.draw_circle(x, y, radius + i*2, False)
    # Draw connecting arcs
    canvas.set_line_width(1)
    for i in range(10):
        start_x = random.randint(400, 1500)
        start_y = random.randint(200, 1000)
        canvas.set_color(0.5, 0.8, 1.0, 0.2)
        canvas.draw_bezier_curve(
            start_x, start_y,
            start_x + 100, start_y - 100,
            start_x + 200, start_y + 100,
            start_x + 300, start_y
        )