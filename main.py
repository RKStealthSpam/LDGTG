import pyglet
import screen_elements
import os
import math
import numpy as np


print(screen_elements.get_elements(12))
window = pyglet.window.Window(height=2048)
window.set_caption("Legally Distinct Geometric Tank Game")

@window.event
def on_draw():
    pass

def image_update(dt):
    window.clear()

pyglet.app.run()