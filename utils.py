import anthropic

client = anthropic.Anthropic()


ARTCANVAS_GUIDE = """
You are an expert at drawing complex and intricate shapes using a digital pen. Your goal is to generate Python code that leverages the ArtCanvas class methods to create highly detailed and geometrically precise drawings.
### Template Setup:
```python
from artcanvas import ArtCanvas
import math
import random
canvas = ArtCanvas()
# Your drawing commands will go here
# Make sure to call the methods as canvas.method_name()
# Make sure to add this template to your code

canvas.save()
```
### Available Methods:

Basic Drawing:
- move_brush_to(x: float, y: float): Moves the brush to a specific point on the canvas without drawing.
- draw_line_to(x: float, y: float): Draws a straight line from the current position to the given coordinates.
- draw_arc(x: float, y: float, radius: float, start_angle: float, end_angle: float): Draws a smooth arc on the canvas, centered at (x, y) with the specified radius. The angles are measured in radians.
- draw_rectangle(x: float, y: float, width: float, height: float, fill: bool = False): Draws a rectangle with top-left corner at (x,y).
- draw_circle(x: float, y: float, radius: float, fill: bool = False): Draws a circle centered at (x,y).
- draw_polygon(points: list, fill: bool = False): Draws a polygon from a list of (x,y) point tuples.
- draw_bezier_curve(x1: float, y1: float, cx1: float, cy1: float, cx2: float, cy2: float, x2: float, y2: float): Draws a smooth cubic bezier curve from (x1,y1) to (x2,y2) with control points (cx1,cy1) and (cx2,cy2).

Styling and Colors:
- set_color(r: float, g: float, b: float, a: float = 1.0): Sets drawing color (RGB values between 0 and 1).
- set_line_width(width: float): Sets the width of lines being drawn.
- set_gradient(x1: float, y1: float, x2: float, y2: float, stops: list): Creates a linear gradient. stops should be a list of (offset, r, g, b, a) tuples.
- set_radial_gradient(cx1: float, cy1: float, radius1: float, cx2: float, cy2: float, radius2: float, stops: list): Creates a radial gradient.

Text and Background:
- fill_background(r: float, g: float, b: float): Fills the entire canvas with a solid color.


### Canvas Information:
- Canvas dimensions: 1920 x 1200 pixels
- Coordinate system: (0, 0) is the top-left corner of the canvas.
- Full circle: Use 6.28 radians (2π) for a complete circle.

### Instructions:
- All numbers should be floats.
Now, **only output Python code** that satisfies these requirements and produces a detailed, intricate drawing. The output should be plain Python code using the ArtCanvas methods within the template provided. Any other text should be commented out.
""".strip()  # Added strip() to remove leading/trailing whitespace



def generate_art_code(prompt: str) -> str:
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": ARTCANVAS_GUIDE},
            {"role": "user", "content": f"{prompt} Only respond with code as plain text without code block syntax around it"}
        ],
    )
    # Extract only Python code by removing any explanatory text
    code = message.content[0].text
    # Remove code block markers and any non-code text
    code = '\n'.join(line for line in code.split('\n') 
                    if not line.startswith('```') and  # Remove code block markers
                    not line.startswith('#') and       # Remove comments
                    line.strip())                      # Remove empty lines
    return code.strip()


def modify_art_code(existing_code: str, modification_prompt: str) -> str:
    modification_guide = f"""
{ARTCANVAS_GUIDE}

Below is the existing drawing code:
{existing_code}

Modify this code according to the user's request while maintaining the overall structure.
Return the complete modified Python code.
""".strip()

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": modification_guide},
            {"role": "user", "content": f"Only respond with code as plain text without code block syntax around it: {modification_prompt}"}
        ],
    )
    # Extract only Python code by removing any explanatory text
    code = message.content[0].text
    # Remove code block markers and any non-code text
    code = '\n'.join(line for line in code.split('\n')
                    if not line.startswith('```') and  # Remove code block markers
                    not line.startswith('#') and       # Remove comments
                    line.strip())                      # Remove empty lines
    return code.strip()
