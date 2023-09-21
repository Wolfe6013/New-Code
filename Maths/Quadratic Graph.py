import turtle
import random

turt = turtle.Turtle()
turt.speed(0)

def grid():    ###----- Makes Grid -----###
    turt.color('light gray')
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

    x = 0-h
    y = 0+l

    turt.up()
    turt.goto(x*10, y*10)
    turt.down()

    while y < 50:
        y = w*(x+h)**2+l
        turt.goto(x*10,y*10)
        x += 0.1

    x = 0-h
    y = 0+l
    turt.up()
    turt.goto(x*10, y*10)
    turt.down()

    while y < 50:
        y = w*(x+h)**2+l
        turt.goto(x*10,y*10)
        x -= 0.1

while True:
    grid()
    parabola()
    spat = input()
    if spat == '':
        turt.clear()
    if spat == 'exit':
        break