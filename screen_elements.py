import pyglet
import sprite_data

def draw_grid(location, width, height, radius):
    batch = pyglet.graphics.Batch()
    spacing = 50
    delta = (spacing * (radius * 2)) / max(width, height)
    x_start = abs(location[0] - radius) % spacing
    y_start = abs(location[1] - radius) % spacing
    # Only references radius area, not screen size
    print(x_start)

    for vert_line in range(int(width / delta) + 1):
        pyglet.shapes.Line(x_start + (vert_line * delta),
                           0,
                           x_start + (vert_line * delta),
                           height,
                           thickness=1,
                           color=(56, 56, 56, 127),
                           batch=batch)

    for horiz_line in range(int(height / delta) + 1):
        pyglet.shapes.Line(x_start + (horiz_line * delta),
                           0,
                           y_start + (horiz_line * delta),
                           height,
                           thickness=1,
                           color=(56, 56, 56, 127),
                           batch=batch)

draw_grid((1500, 350), 1920, 1080, 1000)

def get_elements():
    pass