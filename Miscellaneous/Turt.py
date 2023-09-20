import turtle
import random

turt = turtle.Turtle()
#Colours: #ffffff = white, #000000 = black, #C62828 = red, #9CBA3F = green, #AECF46 = light green
NumberList = [66,"#ffffff",2,"#000000",30,"#ffffff",3,"#000000",30,"#ffffff",3,"#000000",30,"#ffffff",3,"#000000",30,"#ffffff",3,"#000000",30,"#ffffff",3,"#000000",30,"#ffffff",1,"#000000",4,"#C62828",28,"#ffffff",1,"#C62828",2,"#ffffff",4,"#C62828",25,"#ffffff",1,"#C62828",3,"#ffffff",9,"#C62828",19,"#ffffff",2,"#C62828",1,"#ffffff",2,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",4,"#C62828",17,"#ffffff",3,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",2,"#C62828",16,"#ffffff",2,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",2,"#C62828",15,"#ffffff",2,"#C62828",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",2,"#C62828",15,"#ffffff",1,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",2,"#C62828",14,"#ffffff",1,"#C62828",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#C62828",14,"#ffffff",1,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#C62828",14,"#ffffff",1,"#C62828",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#C62828",14,"#ffffff",1,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",2,"#C62828",13,"#ffffff",2,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#C62828",14,"#ffffff",1,"#C62828",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#C62828",14,"#ffffff",1,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#C62828",14,"#ffffff",2,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",2,"#C62828",15,"#ffffff",2,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#C62828",17,"#ffffff",2,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",2,"#C62828",18,"#ffffff",2,"#C62828",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",1,"#9CBA3F",2,"#C62828",20,"#ffffff",5,"#C62828",1,"#AECF46",1,"#9CBA3F",1,"#AECF46",3,"#C62828",25,"#ffffff",5,"#C62828",104,"#ffffff","kiki","kiki"]
turt.speed(0)
turt.hideturtle()

def pixel():
    turt.down()
    turt.forward(9)
    turt.left(90)
    turt.forward(9)
    turt.left(90)
    turt.forward(9)
    turt.left(90)
    turt.forward(9)
    turt.left(90)

def NumberOfColourList():
    Done = 0
    ColourPos = 0
    x = -160
    y = -160
    while Done < 1024:
        turt.up()
        turt.goto(x, y)
        if NumberList[ColourPos] == 0:
            ColourPos += 2
        turt.color(NumberList[ColourPos+1])
        Done += 1
        turt.begin_fill()
        pixel()
        turt.end_fill()
        NumberList[ColourPos] -= 1
        if x == 150:
            y += 10
            x = -160
        else:
            x += 10
        if NumberList[ColourPos] == 0:
                print(f"{Done} done, x = {x}, y = {y}, next colour is {NumberList[ColourPos+1]} for {NumberList[ColourPos+2]} more times")
        else:
            print(f"{Done} done, x = {x}, y = {y}, next colour is {NumberList[ColourPos+3]} for {NumberList[ColourPos]} more times")

NumberOfColourList()
input('')