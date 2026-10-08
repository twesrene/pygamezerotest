import pgzrun

WIDTH = 300 
HEIGHT = 300 

TITLE = "Clicker" 
FPS = 30 
count = 0

def draw():
    screen.fill((175, 228, 222)) #using rgb colour
    screen.draw.text(str(count), center=(150, 150), color="black", fontsize = 96)
    
def on_mouse_down(button, pos):
    global count
    if button == mouse.LEFT:
        count = count + 1
      
pgzrun.go()
