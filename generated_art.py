from artcanvas import ArtCanvas
import math
import random
canvas = ArtCanvas()
canvas.fill_background(0.05, 0.05, 0.15)
for _ in range(300):
    x = random.uniform(0, 1920)
    y = random.uniform(0, 600)
    size = random.uniform(1.0, 3.0)
    brightness = random.uniform(0.6, 1.0)
    canvas.set_color(brightness, brightness, brightness, brightness)
    canvas.draw_circle(x, y, size, True)
canvas.set_gradient(0, 300, 0, 1200, [
    (0.0, 0.1, 0.2, 0.4, 0.8),
    (0.5, 0.2, 0.3, 0.5, 0.6),
    (1.0, 0.0, 0.0, 0.2, 0.4)
])
for x in range(0, 1920, 80):
    height = random.uniform(400, 800)
    width = random.uniform(30, 60)
    canvas.draw_rectangle(x, 1200-height, width, height, True)
    # Add glowing windows
    canvas.set_color(0.3, 0.8, 1.0, 0.8)
    for y in range(int(1200-height), 1200, 30):
        for wx in range(int(x+5), int(x+width-5), 15):
            if random.random() > 0.3:
                canvas.draw_rectangle(wx, y, 8, 15, True)
for _ in range(50):
    x = random.uniform(0, 1920)
    y = random.uniform(300, 1000)
    canvas.set_color(1.0, 1.0, 0.3, 0.6)
    canvas.draw_circle(x, y, 3, True)
    canvas.draw_line_to(x-15, y)
for _ in range(10):
    x = random.uniform(100, 1800)
    y = random.uniform(400, 800)
    canvas.set_color(0.2, 0.5, 0.8, 0.7)
    canvas.draw_circle(x, y, 40, True)
    canvas.set_color(0.3, 0.6, 0.9, 0.8)
    canvas.draw_circle(x, y, 35, True)
for _ in range(15):
    x1 = random.uniform(0, 1920)
    y1 = random.uniform(600, 1000)
    x2 = x1 + random.uniform(-200, 200)
    y2 = y1 + random.uniform(-200, 200)
    canvas.set_color(0.2, 0.8, 1.0, 0.3)
    canvas.set_line_width(5.0)
    canvas.move_brush_to(x1, y1)
    canvas.draw_line_to(x2, y2)
for _ in range(5):
    x = random.uniform(200, 1700)
    y = random.uniform(300, 700)
    size = random.uniform(50, 100)
    canvas.set_color(0.3, 0.8, 1.0, 0.2)
    canvas.draw_rectangle(x, y, size*2, size, True)
canvas.save()