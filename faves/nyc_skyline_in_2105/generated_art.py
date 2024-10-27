from artcanvas import ArtCanvas
import math
import random
with ArtCanvas() as canvas:
    # Background - night sky gradient
    canvas.set_gradient(0, 0, 0, 1200, [(0, 0.05, 0.05, 0.2, 1), (1, 0, 0, 0.1, 1)])
    canvas.fill_background(0, 0, 0.1)
    # Stars
    for _ in range(300):
        x = random.uniform(0, 1920)
        y = random.uniform(0, 600)
        size = random.uniform(1, 3)
        canvas.set_color(1, 1, random.uniform(0.8, 1), random.uniform(0.3, 0.9))
        canvas.draw_circle(x, y, size, True)
    # Base city glow
    canvas.set_radial_gradient(960, 1000, 800, 960, 1000, 100,
                             [(0, 0.2, 0.4, 0.6, 0.1), (1, 0.1, 0.2, 0.4, 0)])
    canvas.draw_circle(960, 1000, 800, True)
    # Futuristic buildings
    for x in range(0, 1920, 60):
        height = random.uniform(300, 800)
        width = random.uniform(30, 50)
        # Building base
        canvas.set_color(0.1, 0.2, 0.3, 0.9)
        canvas.draw_rectangle(x, 1200-height, width, height, True)
        # Glowing windows
        for y in range(int(1200-height), 1200, 30):
            if random.random() > 0.3:
                canvas.set_color(0.3, 0.8, 1, random.uniform(0.3, 0.8))
                canvas.draw_rectangle(x+5, y, width-10, 15, True)
        # Spires and antennas
        if random.random() > 0.7:
            canvas.set_color(0.2, 0.3, 0.4, 0.9)
            canvas.set_line_width(2)
            canvas.move_brush_to(x + width/2, 1200-height)
            canvas.draw_line_to(x + width/2, 1200-height-random.uniform(50, 150))
    # Floating vehicles
    for _ in range(50):
        x = random.uniform(0, 1920)
        y = random.uniform(200, 800)
        # Vehicle lights
        canvas.set_color(1, 0.8, 0.2, 0.6)
        canvas.draw_circle(x, y, 3, True)
        canvas.set_color(1, 0.8, 0.2, 0.2)
        canvas.draw_circle(x+random.uniform(2, 5), y, 8, True)
    # Holographic advertisements
    for _ in range(10):
        x = random.uniform(100, 1820)
        y = random.uniform(300, 700)
        size = random.uniform(50, 150)
        canvas.set_color(0.3, 0.8, 1, 0.2)
        canvas.draw_rectangle(x, y, size, size/2, True)
        canvas.set_color(0.3, 0.8, 1, 0.4)
        canvas.draw_rectangle(x+5, y+5, size-10, size/2-10, False)
    # Energy beams
    for _ in range(5):
        x1 = random.uniform(0, 1920)
        y1 = random.uniform(600, 1000)
        x2 = x1 + random.uniform(-200, 200)
        y2 = y1 - random.uniform(100, 300)
        canvas