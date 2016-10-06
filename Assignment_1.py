# Assignment 1 for MIS3640


''' Problem 1 - Prime Factors of Integers '''


import math

n = input ("Enter integer: ")
n = int(n)
l = []

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False

    if n == 2:
        return True 

    if not n & 1:
        return False

    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def prime (n):
    if(math.floor((n+1)/2) == 2):
        if(n%i == 0):
            l.append(i)
            n = n/i
            return(n)

while(True):
    if(isprime(n) == False):
        n = prime(n)

    else:
        l.append(math.floor(n))
        break

print(l)



