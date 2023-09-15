import turtle
import random
import time

turtle.bgcolor('#653cc2')

def duobirdBd():
    Jinn = turtle.Turtle()
    Jinn.color('#79c902')

    Jinn.fillcolor('#79c902')

    Jinn.speed(0)

    Jinn.hideturtle()

 

    Jinn.up()

    Jinn.begin_fill()

    Jinn.setpos(100+x,0+y)

    Jinn.down()

    Jinn.right(90)

    Jinn.forward(20)

    Jinn.left(45)

    Jinn.forward(80)

    Jinn.left(180)

    Jinn.circle(20,-90)

    Jinn.right(35)

    Jinn.circle(175,-25)

    Jinn.setheading(90)

    Jinn.right(15)

    Jinn.circle(85,-148)

    Jinn.left(88)

    Jinn.circle(175,-25)

    Jinn.right(34)

    Jinn.circle(20,-90)

    Jinn.setpos(-100+x,-20+y)

    Jinn.setpos(-100+x,50+y)

    Jinn.setheading(270)

    Jinn.circle(35,-125)

    Jinn.left(180)

    Jinn.circle(79,69)

    Jinn.setheading(216)

    Jinn.circle(35,-125)

    Jinn.setpos(100+x,50+y)

    Jinn.setpos(100+x,0+y)

    Jinn.end_fill()



 

def duobirdFt():

    Feet = turtle.Turtle()

    Feet.color('#f59101')

    Feet.fillcolor('#f59101')

    Feet.speed(100)

    Feet.hideturtle()

 

    Feet.up()

    Feet.setpos(50+x,-147+y)

    Feet.down()

    Feet.begin_fill()

    Feet.right(180)

    Feet.circle(15,-180)

    Feet.setheading(180)

    Feet.forward(25)

    Feet.right(180)

    Feet.circle(20,-70)

    Feet.setheading(5)

    Feet.circle(85,33)

    Feet.end_fill()

 

    Feet.up()

    Feet.setpos(-55+x,-147+y)

    Feet.down()

    Feet.begin_fill()

    Feet.setheading(180)

    Feet.circle(15,180)

    Feet.forward(25)

    Feet.right(180)

    Feet.setheading(0)

    Feet.circle(20,70)

    Feet.setheading(354)

    Feet.circle(85,-33)

    Feet.end_fill()   



 

def duobirdC():

    Chest = turtle.Turtle()

    Chest.color('#8fdf01')

    Chest.fillcolor('#8fdf01')

    Chest.speed(0)

    Chest.hideturtle()

 

    Chest.up()

    Chest.setpos(0+x, -100+y)

    Chest.down()

    Chest.begin_fill()

    Chest.forward(15)

    Chest.left(90)

    Chest.circle(15,-180)

    Chest.left(90)

    Chest.forward(15)

    Chest.end_fill()

 

    Chest.up()

    Chest.setpos(25+x, -75+y)

    Chest.down()

    Chest.begin_fill()

    Chest.forward(15)

    Chest.left(90)

    Chest.circle(15,-180)

    Chest.left(90)

    Chest.forward(15)

    Chest.end_fill()

 

    Chest.up()

    Chest.setpos(-25+x, -75+y)

    Chest.down()

    Chest.begin_fill()

    Chest.forward(15)

    Chest.left(90)

    Chest.circle(15,-180)

    Chest.left(90)

    Chest.forward(15)

    Chest.end_fill()   


 

def duobirdFc():

    Face = turtle.Turtle()

    Face.color('#8ede01')

    Face.fillcolor('#8ede01')

    Face.speed(0)

    Face.hideturtle()

 

    Face.up()

    Face.setpos(20+x,30+y)

    Face.down()

    Face.begin_fill()

    Face.left(45)

    Face.forward(45)

    Face.right(265)

    Face.circle(18,-90)

    Face.setheading(45)

    Face.forward(20)

    Face.right(265)

    Face.circle(13,-90)

    Face.setheading(180)

    Face.circle(18,-90)

    Face.right(180)

    Face.forward(35)

    Face.right(180)

    Face.circle(35,-145)

    Face.right(160)

    Face.forward(12)

    Face.up()

    Face.setpos(20+x,30+y)

    Face.setheading(45)

    Face.down()

    Face.circle(35,-90)

    Face.right(180)

    Face.forward(45)

    Face.right(265)

    Face.circle(18,90)

    Face.setheading(135)

    Face.forward(20)

    Face.right(265)

    Face.circle(13,90)

    Face.setheading(180)

    Face.circle(18,90)

    Face.forward(35)

    Face.circle(35,145)

    Face.right(20)

    Face.forward(12)

    Face.setheading(0)

    Face.forward(30)

    Face.end_fill()


 

def duobirdBk():

    Beak = turtle.Turtle()

    Beak.color('#f49203')

    Beak.fillcolor('#f49203')

    Beak.speed(0)

    Beak.hideturtle()

 

    Beak.up()

    Beak.setpos(-16+x,-25+y)

    Beak.down()

    Beak.begin_fill()

    Beak.setheading(272)

    Beak.circle(15,180)

    Beak.end_fill()

 

    Beak.color('#fec301')

    Beak.fillcolor('#fec301')

 

    Beak.up()

    Beak.setheading(0)

    Beak.setpos(-20+x,-23+y)

    Beak.down()

    Beak.begin_fill()

    Beak.right(135)

    Beak.circle(27,-90)

    Beak.setheading(195)

    Beak.forward(20)

    Beak.right(30)

    Beak.forward(20)

    Beak.end_fill()


 

def duobirdE():

    Eye = turtle.Turtle()

    Eye.color('#fefeff')

    Eye.fillcolor('#fefeff')

    Eye.speed(0)

    Eye.hideturtle()

 

    Eye.up()

    Eye.setpos(30+x,-17+y)

    Eye.down()

    Eye.begin_fill()

    Eye.right(90)

    Eye.circle(23,180)

    Eye.forward(18)

    Eye.circle(23,180)

    Eye.forward(18)

    Eye.end_fill()

    Eye.up()

    Eye.setheading(0)

    Eye.setpos(-76+x,-17+y)

    Eye.down()

    Eye.begin_fill()

    Eye.right(90)

    Eye.circle(23,180)

    Eye.forward(18)

    Eye.circle(23,180)

    Eye.forward(18)

    Eye.end_fill()

 

    Eye.color('#4a4a4b')

    Eye.fillcolor('#4a4a4b')

 

    Eye.up()

    Eye.setpos(38+x,-14+y)

    Eye.setheading(0)

    Eye.down()

    Eye.begin_fill()

    Eye.right(90)

    Eye.circle(10,180)

    Eye.forward(14)

    Eye.circle(10,120)

    Eye.right(60)

    Eye.circle(7,-160)

    Eye.setheading(270)

    Eye.forward(10)

    Eye.end_fill()

 

    Eye.up()

    Eye.setpos(-58+x,-14+y)

    Eye.setheading(0)

    Eye.down()

    Eye.begin_fill()

    Eye.right(90)

    Eye.circle(10,180)

    Eye.forward(14)

    Eye.circle(10,120)

    Eye.right(60)

    Eye.circle(7,-160)

    Eye.setheading(270)

    Eye.forward(10)

    Eye.end_fill()


def FullBird():
    duobirdBd()
    duobirdFt()
    duobirdC()
    duobirdFc()
    duobirdBk()
    duobirdE()

clear = turtle.Turtle()
clear.speed(0)
clear.color('#653cc2')

while True:
    clear.begin_fill()
    clear.goto(-500, -500)
    clear.goto(-500, 500)
    clear.goto(500,500)
    clear.goto(500,-500)
    clear.goto(-500,-500)
    clear.end_fill()

    x = random.randint(-70,70)*5
    y = random.randint(-50,50)*5
    
    FullBird()
    h = input('Again? (y/n) ')
    if h == 'n':
        break