import turtle
import random

turt = turtle.Turtle()
turt.speed(0)
coloursList = ['red','orange','green','blue','purple','#ff4081']

def grid():    ###----- Makes Grid -----###
    turt.color('#d4d7d8') ###light gray##
    gridX = -400
    while gridX <= 400:
        turt.up()
        turt.goto(gridX, -400)
        turt.down()
        turt.goto(gridX, 400)
        gridX+=10
    gridY = -400
    while gridY <= 400:
        turt.up()
        turt.goto(-400, gridY)
        turt.down()
        turt.goto(400, gridY)
        gridY+=10
    turt.color('#696e70') ###gray##
    gridX = -400
    while gridX <= 400:
        turt.up()
        turt.goto(gridX, -400)
        turt.down()
        turt.goto(gridX, 400)
        gridX+=50
    gridY = -400
    while gridY <= 400:
        turt.up()
        turt.goto(-400, gridY)
        turt.down()
        turt.goto(400, gridY)
        gridY+=50
    turt.color('#000000') ##black###
    turt.up()
    turt.goto(-400, 0)
    turt.down()
    turt.goto(400, 0)
    turt.up()
    turt.goto(0, -400)
    turt.down()
    turt.goto(0, 400)

def parabola():    ###----- Makes Parabola -----###
    w  = float(input('y = '))
    h = float(input('y = w(x + '))
    l = float(input('y = w(x + h)^2 + '))
    colour = input('Colour of line? ')
    if colour == '':
        colour = random.choice(coloursList)

    turt.color(colour)
    
    x = 0-h
    y = 0+l

    turt.up()
    turt.goto(x*10, y*10)
    turt.down()

    while y < 50 and y > -50:
        y = w*(x+h)**2+l
        turt.goto(x*10,y*10)
        x += 0.1

    x = 0-h
    y = 0+l
    turt.up()
    turt.goto(x*10, y*10)
    turt.down()

    while y < 50 and y > -50:
        y = w*(x+h)**2+l
        turt.goto(x*10,y*10)
        x -= 0.1

grid()
while True:
    parabola()
    spat = input()
    if spat == 'clear':
        turt.clear()
        grid()
    if spat == 'exit':
        break