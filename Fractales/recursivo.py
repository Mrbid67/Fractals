import turtle as tortuguita
import numpy as np
import random

partyMode = True

def drawTriangle(points,color ,myTurtle):
    if(partyMode):
        color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()


def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,miTortuguita):
    color = ['white', 'black']
    drawTriangle(points, color[degree % 2],miTortuguita)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, miTortuguita)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, miTortuguita)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, miTortuguita)

def main():
   miTortuguita = tortuguita.Turtle()
   miTortuguita.hideturtle()
   #Hacemos que la tortuguita pille nitro.
   miTortuguita.speed(0)
   win = tortuguita.Screen()
   win.bgcolor("white")
   puntos = [[-400,-300],[0,300],[400,-300]]
   sierpinski(puntos,5,miTortuguita)
   win.exitonclick()
  

main()
