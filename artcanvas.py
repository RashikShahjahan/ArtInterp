import math
import cairo

class ArtCanvas:
    def __init__(self, width=1920, height=1200, filename="output.png"):
        # Initialize canvas
        self.surface = None
        self.ctx = None
        self.width = width
        self.height = height
        self.filename = filename

    def __enter__(self):
        # Initialize canvas when entering context
        self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.width, self.height)
        self.ctx = cairo.Context(self.surface)
        
        # Set default white background
        self.ctx.set_source_rgb(1, 1, 1)
        self.ctx.paint()
        self.ctx.set_line_width(1)
        self.ctx.set_source_rgb(0, 0, 0)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Save the image before cleanup
        if self.surface:
            self.surface.write_to_png(self.filename)
            self.surface.finish()

    def move_brush_to(self, x, y):
        self.ctx.move_to(x, y)

    def draw_line_to(self, x, y):
        self.ctx.line_to(x, y)
        self.ctx.stroke()  # Add this line to make the path visible
        self.ctx.move_to(x, y)  # Move to end point for next line

    def draw_arc(self, xc, yc, radius, start_angle, end_angle):
        # move to start point the circumference of the arc
        self.ctx.move_to(xc + radius * math.cos(start_angle), yc + radius * math.sin(start_angle))
        self.ctx.arc(xc, yc, radius, start_angle, end_angle)
        self.ctx.stroke()  # Add this line to make the arc visible

    def draw_rectangle(self, x, y, width, height, fill=False):
        """Draw a rectangle with top-left corner at (x,y)"""
        self.ctx.rectangle(x, y, width, height)
        if fill:
            self.ctx.fill()
        else:
            self.ctx.stroke()

    def draw_circle(self, x, y, radius, fill=False):
        """Draw a circle centered at (x,y)"""
        self.ctx.arc(x, y, radius, 0, 2 * math.pi)
        if fill:
            self.ctx.fill()
        else:
            self.ctx.stroke()

    def set_color(self, r, g, b, a=1.0):
        """Set drawing color (RGB values between 0 and 1)"""
        self.ctx.set_source_rgba(r, g, b, a)

    def set_line_width(self, width):
        """Set the width of lines being drawn"""
        self.ctx.set_line_width(width)

    def draw_text(self, x, y, text, font_size=16, font_family="Sans"):
        """Draw text at position (x,y)"""
        self.ctx.select_font_face(font_family)
        self.ctx.set_font_size(font_size)
        self.ctx.move_to(x, y)
        self.ctx.show_text(text)

    def fill_background(self, r, g, b):
        """Fill the entire canvas with a solid color"""
        self.ctx.set_source_rgb(r, g, b)
        self.ctx.paint()
        self.ctx.set_source_rgb(0, 0, 0)  # Reset to black


 
