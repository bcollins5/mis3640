# Exercise 2
# Question 3


a = int(input('1st integer is '))
b = int(input('2nd integer is '))


def gcd(m,n):
    z=abs(m-n)
    if (m-n) == 0:
        return n
    else:
        return gcd(z,min(m,n))


print(gcd(a,b))



#Tower of Hanoi problem



