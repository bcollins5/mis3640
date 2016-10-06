list_1 = [10, 20]

AFC_east = ['New England Patriots', 'Buffalo Bills',
             'Miami Dolphins', 'New York Jets']


a_nested_list = ['spam', 2.0, 5, [10,20]]
print(AFC_east)

AFC_east[3] = 'New York Giants'   #replaces fourth team with Giants
print(AFC_east)

print(AFC_east[0:2])
print(AFC_east[-2:])          # -integer is going backwards   prints last two teams


L = [
    ['Apple', 'Google', 'Microsoft'],                    #nested list
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]


print(L[0][0])      #finds Apple 
print(L[2][2])      #finds Lisa
print(L[1][2][1])   #finds On Rail



for team in AFC_east:
    print(team)




'''Traversing a list'''
numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)  




my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]

print(len(my_list))


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b             #combines the two list into a single list
print(c)


m = []
m.append(a)
m.append(b)
print(m)


print([0] * 4)
print(['Tom Brady', 'Bill Belichick'] * 3)


t = ['a', 'b', 'c', 'd', 'e', 'f']

print(t[1:3])
print(t[:4])
print(t[3:])


t[1:3] = ['x', 'y']
print(t)


'''List Methods - Exercise 3'''

t = ['a', 'b', 'c']
t.append('d')
print(t)


list.remove('b')
print(t)