import turtle

'''
#Excercise 2.1
def square(t):
    for i in range(4):     #we repeat same thing four times
        t.fd(100)
        t.lt(90)

'''



#Exercise 2.2

def square(t, length):
    for i in range(4):     #we repeat same thing four times
        t.fd(length)
        t.lt(90)


#Exercise 2.3
def square(t, length):
    for i in range(n):     #we repeat same thing four times
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


'''
def square(t, length):
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)



'''    

'''
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

#teresa = turtle.Turtle()
#square(teresa)


turtle.mainloop()
'''