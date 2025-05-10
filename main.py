import pyglet
import screen_elements
import sprite_data
import os
import math
import numpy as np


# Main Run Window Setup
display = pyglet.display.get_display()
screen = display.get_default_screen()
window = pyglet.window.Window(width=int(screen.width/2),
                              height=round(screen.height/2),
                              resizable=True)
window.set_location(round(screen.width/4), round(screen.height/4))
window.set_caption("Legally Distinct Geometric Tank Game")


player_tank = sprite_data.Tank((0, 0), 0, 0, 0)

@window.event()
def on_resize(width, height):
    print(f'Window resized to {width}, {height}')


@window.event
def on_draw():
    pass

@window.event
def on_key_press(symbol, modifier):
    if symbol == pyglet.window.key.W or symbol == pyglet.window.key.UP:
        player_tank.set_acceleration((player_tank.acceleration[0], player_tank.acceleration[1] + 1))
    if symbol == pyglet.window.key.A or symbol == pyglet.window.key.LEFT:
        player_tank.set_acceleration((player_tank.acceleration[0] - 1, player_tank.acceleration[1]))
    if symbol == pyglet.window.key.S or symbol == pyglet.window.key.DOWN:
        player_tank.set_acceleration((player_tank.acceleration[0], player_tank.acceleration[1] - 1))
    if symbol == pyglet.window.key.D or symbol == pyglet.window.key.RIGHT:
        player_tank.set_acceleration((player_tank.acceleration[0] + 1, player_tank.acceleration[1]))

@window.event
def on_key_release(symbol, modifier):
    if symbol == pyglet.window.key.W or symbol == pyglet.window.key.UP:
        player_tank.set_acceleration((player_tank.acceleration[0], player_tank.acceleration[1] - 1))
    if symbol == pyglet.window.key.A or symbol == pyglet.window.key.LEFT:
        player_tank.set_acceleration((player_tank.acceleration[0] + 1, player_tank.acceleration[1]))
    if symbol == pyglet.window.key.S or symbol == pyglet.window.key.DOWN:
        player_tank.set_acceleration((player_tank.acceleration[0], player_tank.acceleration[1] + 1))
    if symbol == pyglet.window.key.D or symbol == pyglet.window.key.RIGHT:
        player_tank.set_acceleration((player_tank.acceleration[0] - 1, player_tank.acceleration[1]))

    print(symbol)

def image_update(dt):
    window.clear()

pyglet.app.run()
