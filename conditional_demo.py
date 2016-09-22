
'''
age = int(input('How old are you?'))
if age > 21:
    print('Your age is {}.'.format(age))
    print('Your age is ' + str(age) + '.')
    print('Yes, you can.')
elif age >= 6:
    print('Your age is ', age)
    print('You are a teenager. No, you cannot.')
else:
    print('Your age is ', age)
    print('No, not allowed.')




# Nested
x = 1 
y = 2

if x == y:
    print('x and y are equal.')
else:
    if x < y:
        print('x is less than y.')
    else:
        print('x is greater than y')
'''



'''
#Exercise 1

print('BMI calculator - US Version')

weight = input('enter weight in pounds')
height = input('enter height in inches')
weight = float(weight)
height = float(height)


bmi = (703*((weight/(height**2))))


if bmi <= 18.5:
    print('BMI is %.1f. You are a scrawny lil bih')

elif 18.5 < bmi <= 25:
    print('BMI is %.1f. U gucci louis prada, scuse me')

elif 25 < bmi <= 29.9:
    print('BMI is %.1f. Damn, g you fat. checkit')

else:
    print('BMI is %.1f. AYOO Baby Beluga')

'''    


'''
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(3)

def print_n(s,n):
    if n<= 0:
        return
    print(s)
    print('n =', n)
    print_n(s, n-1)

print_n('Hello', 3)



#Exercise 2
#Problem 1 - factorials


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(1))
print(factorial(3))
print(factorial(5))



#Problem 2 - fibonacci

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(3))
print(fib(4))
print(fib(10))

    
'''

a = int(input('1st integer is '))
b = int(input('2nd integer is '))


def gcd(m,n):
    z=abs(m-n)
    if (m-n) == 0:
        return n
    else:
        return gcd(z,min(m,n))


print(gcd(a,b))


