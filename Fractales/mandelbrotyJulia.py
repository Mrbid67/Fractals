from cmath import sqrt
from PIL import Image
import numpy as np
import colorsys

# Tamanho de pantalla
WIDTH = 1920
HEIGHT = 1080

hacerJulia = False
hacerMandel = True

def rgb_conv(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 50.0, 1.0, 0.5))
    return tuple(color.astype(int))
  
# function defining a mandelbrot
def mandelbrot(x, y):
    c0 = np.complex(x, y)
    c = c0
    for i in range(1, 100):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c*c + c0
    return (0, 0, 0)

def julia(x,y,c1, c2):
    
    c = np.complex(x, y)
    c0 = np.complex(c1,c2)

    for i in range(1, 100):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c*c + c0

    return(0,0,0)
  
# creating the new image in RGB mode
img = Image.new('RGB', (WIDTH, HEIGHT))
pixels = img.load()

if(hacerMandel):
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixels[x, y] = mandelbrot((x - (0.75 * WIDTH)) / (WIDTH / 4),
                                        (y - (WIDTH / 4)) / (WIDTH / 4))
    img.save("mandelbrot.png")

if(hacerJulia):
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixels[x, y] = julia(1.5*(x - WIDTH/2)/(0.5*WIDTH), 1.5*(y - HEIGHT/2)/(0.5*HEIGHT), -0.7, 0.27015)
    img.save("julia.png")

img.show()