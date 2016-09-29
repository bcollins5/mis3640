#Class Session 
'''
result = 0
for i in range(11):
    result += i          # means: result = result + i


print(result)
'''

'''
result = 0
for i in range(1,11,2):          #for even change to 0
    if i % 2 == 1:               #for even change to 0
        print('current i: ', i)
        result += i

print(result)
'''

'''
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

countdown(5)
'''


'''
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
'''


'''
iteration = 0                #this is resetting the count for each letter
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
'''


'''
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
'''

'''
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')
'''



#Rewriting exercise 1 with while statement
'''
result = 0
i = 1
while i < 11: 
    result = result + i
    i = i + 1

print(result)
'''


result = 0
i = 1
while i <= 10:
    if i % 2 == 0: 
        result = result + i
    
    i = i + 1

print(result)