inport pgzrun
from random import randint

widht = 300
height = 300

def draw():
    r = 255
    g = 0 
    b = randit(120, 255)
    
    width = WIDTH
    height = HEIGHT - 200
    
    for i in range(20):
        rect = Rect ((0, 0),( (width, height))
        rect.centre =150, 150
        screen.draw.rect(rect, (r, g, b))            
                     
        r-= 10
        g+= 10
        
        width-= 10
        hieght+= 10