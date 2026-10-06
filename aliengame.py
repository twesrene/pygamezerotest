import pgzrun
from pgzhelper import *

WIDTH = 700 
HEIGHT = 400 

TITLE = "Usagi Runner"
FPS = 30


alien = Actor('usagistand', (50, 240))
alien.scale = 0.8
background = Actor("background")
alien.angle = 120


def draw():
    background.draw()
    alien.draw()
    
def update(dt):
    alien.x = alien.x + 5
    alien.angle = alien.angle + 10

pgzrun.go()
