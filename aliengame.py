import pgzrun
from pgzhelper import *

WIDTH = 700 
HEIGHT = 400 

TITLE = "Usagi Runner" 
FPS = 30

alien = Actor('usagistand', (50, 240))
background = Actor("background")

def draw():
    background.draw()
    alien.draw()

def update(dt):
    if keyboard.left and alien.x > 20:
        alien.x = alien.x - 5
    elif keyboard.right and alien.x < 650:
        alien.x = alien.x + 5
        
    if keyboard.space:
        alien.y = alien.y - 10
        animate(alien, tween='bounce_end',duration=1, y = 240)

pgzrun.go()
