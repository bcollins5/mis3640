'''#import turtle


#Excercise 2.1
def square(t):
    for i in range(4):     #we repeat same thing four times
        t.fd(100)
        t.lt(90)

'''


'''
#Exercise 2.2

def square(t, length):
    for i in range(4):     #we repeat same thing four times
        t.fd(length)
        t.lt(90)


#Exercise 2.3
def square(t, length):
    for i in range(n):     #we repeat same thing n times
        t.fd(length)
        t.lt(360/n)



jerry = turtle.Turtle()
#square(jerry, 100)
#polygon(jerry,50,12)           #change 12 to 4 for a square

alex = turtle.Turtle()
#polygon(alex, 30, 8)


polygon(alex, n=7, length=70)
polygon(alex, 70, 7)


turtle.mainloop()





#Exercise 2.4



def square(t, length):
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)



    

def polygon(t, length, n):
    #needed to be modified
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)

    



jerry = turtle.Turtle()

square(jerry)

teresa = turtle.Turtle()
square(teresa)


turtle.mainloop()
'''

#  Yin & Yang with some color
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from turtle import *

def yin(radius, color1, color2):
    width(3)
    color("black", color1)
    begin_fill()
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    #mainloop()




#  Practicing around with some other designs
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





'The Number 3 ... working on the 0 part, for #30'
'Trying to create a jersey image throughout the semester, maybe'


import turtle
jerry = turtle.Turtle()
print(jerry)



def square(t, length):
    for i in range(4):     #we repeat same thing n times
        t.fd(length)
        t.lt(90)

square(jerry, 100)

jerry.fd(100)

square(jerry, 100)

jerry.fd(100)

square(jerry, 100)

jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)

square(jerry, 100)

jerry.fd(100)

square(jerry, 100)
jerry.rt(180)
jerry.fd(100)
jerry.rt(90)
jerry.fd(200)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.fd(100)
jerry.rt(90)
jerry.fd(300)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(180)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(90)
jerry.fd(100)
jerry.rt(270)



turtle.mainloop()


'''def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


polygon(jerry, 7, 70)'''


