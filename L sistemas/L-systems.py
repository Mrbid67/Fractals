import turtle

hacerKoch = True
hacerSierpinsky = False
hacerSierpinskyCarpet = False

def generarSistema(iters, char):
    strBase = char
    strReglas = ""
    for i in range (iters):
        aux = ""
        for ch in strBase:
            if(hacerKoch):
                aux = aux + reglasKoch(ch)
            elif(hacerSierpinsky):
                aux = aux + reglasSierpinsky(ch)
            elif(hacerSierpinskyCarpet):
                aux = aux + reglasSierpinskyCarpet(ch)
        strReglas = aux
        strBase = strReglas
    return strReglas
    
    

def reglasKoch(char):
    reglaAplicada = ""

    if char == 'F':
        reglaAplicada = 'F+F-F-F+F'   #SI encontramos un F generamos: Forward, -60 grados, Forward, +60g, +60g, forward, -60g, forward
    else:
        reglaAplicada = char    # no aplicamos la regla

    return reglaAplicada

def reglasSierpinsky(char):
    reglaAplicada = ""

    if char == 'A':
        reglaAplicada = 'B-A-B'   
    elif char == 'B':
        reglaAplicada = 'A+B+A'
    else:
        reglaAplicada = char    # no aplicamos la regla

    return reglaAplicada


def reglasSierpinskyCarpet(char):
    reglaAplicada = ""

    if char == 'F':
        reglaAplicada = 'F+F-F-F-G+F+F+F-F'   
    elif char == 'G':
        reglaAplicada = 'GGG'
    else:
        reglaAplicada = char    # no aplicamos la regla

    return reglaAplicada

def dibujarLsystem(tortuga, instructions, angle, distance):
    for char in instructions:
        if char == 'F' or char == 'G':
            tortuga.forward(distance)
        elif char == 'B' or char == 'A':
            tortuga.backward(distance)
        elif char == '+':
            tortuga.right(angle)
        elif char == '-':
            tortuga.left(angle)


t = turtle.Turtle()          
wn = turtle.Screen()

if(hacerKoch):
        
    t.up()
    t.back(200)
    t.down()
    t.speed(0)
    inst = generarSistema(4, "F")   # Creamos el string de reglas
    print(inst)
    dibujarLsystem(t, inst, 90, 5)   

elif(hacerSierpinsky):
    t.speed(0)
    inst = generarSistema(6, "A")   # Creamos el string de reglas
    dibujarLsystem(t, inst, 60, 5)   

elif(hacerSierpinskyCarpet):
    t.speed(0)
    inst = generarSistema(4, "F")   # Creamos el string de reglas
    dibujarLsystem(t, inst, 90, 4)   
wn.exitonclick()


