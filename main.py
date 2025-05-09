import pyglet
import screen_elements
import sprite_data
import os
import math
import numpy as np


print(screen_elements.get_elements(12))
# Main Run Window Setup
display = pyglet.display.get_display()
screen = display.get_default_screen()
window = pyglet.window.Window(width=int(screen.width/2),
                              height=round(screen.height/2),
                              resizable=True)
window.set_location(round(screen.width/4), round(screen.height/4))
window.set_caption("Legally Distinct Geometric Tank Game")


@window.event()
def on_resize(width, height):
    print(f'Window resized to {width}, {height}')


@window.event
def on_draw():
    pass

def image_update(dt):
    window.clear()

pyglet.app.run()
