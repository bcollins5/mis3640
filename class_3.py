#def print_lyrics():
    #print("Hey Jude. Don't make it bad.")
    #print("Take a sad song and make it better.")



#print(type(print_lyrics))
#print_lyrics()



#def repeat_lyrics():
    #print_lyrics()
    #print('Na - na - na - na - na - na - na - na - na -na - na')
    #print_lyrics()


#repeat_lyrics()


#def print_twice(a):
    #print(a)
    #print(a)

#print_twice('Babson')



#my_name = 'Jerry'
#print_twice(my_name)

#input()



#def my_abs(n):
    #if isinstance(n, int) or isinstance(n, float):
        #if n >= 0:
            #return n
        #else:
            #return -n
    #else:
        #print('invalid value')


#print(my_abs(100))

#print(my_abs(0))

#print(my_abs(-4))

#print(my_abs('a'))


#def cat_twice(part1, part2):
    #cat = part1 + part2
    #print_twice(cat)


#line1 = 'Bing tiddle '
#line2 = 'Tiddle bang.'
#cat_twice(line1, line2)

#print(line1)


#def give_me_a_break():
    #str1 = 'break'
    #return str1
    #print('another break')



#def give_me_a_break():
    #str1 = 'break'
    #print('another break')
    #return str1



#give_me_a_break()
#print(give_me_a_break())



def quad():


    # from math import sqrt
    # from math import *
    # x**0.5

    from math import sqrt
    print("This program will find the roots of a quadratic equation")
    print()

    a= int(input("integer for first coefficient: "))
    b= int(input("integer for second coefficient: "))
    c= int(input("integer for third coefficient: "))
    print()
    disc = b**2 - 4*a*c    #b^2 - 4ac
    disc1 = sqrt(disc)     #value of discriminant
    positive = (-b + disc1) / (2*a)
    negative = (-b - disc1) / (2*a)

    print("the positive value of the quadratic equation is {0}, and the negative value is {1}". format(positive,negative))

quad()

#pull up command window to input the first, second, and third coefficients