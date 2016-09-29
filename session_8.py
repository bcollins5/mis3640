team = 'New England Patriots'
#print(team[0:11])
#print(team[12:20])

#print(team[:11])
#print(team[12:])


#new_team = team[:12]+'Seahawks'
#print(new_team)

#print(team)

# def find(word, letter):
    # index = 0
    # while index < len(word):
        # if word[index] == letter:
            # return index
        # index = index + 1
    # return -1

#print(find(team, 'E'))

'''
#Exercise 3 - 
?????? What does this mean???
"so that it accepts the string ..and the letter...<-- as arguments."
(im finding no help online)
'''

# word = 'New England Patriots'
# count = 0
# for letter in word:
    # if letter == 'a':
        # count = count + 1
# print(count)


# word = 'superkalifrajilisticexpeiallodocious'
# count = 0
# for letter in word:
    # if letter == 'i':
        # count = count + 1

# print (count)


# def find(word, letter):
    # index = 0
    # while index < len(word):
        # if word[index] == letter:
            # return index
        # index = index + 1
    # return -1


#print(find(team, 'P'))



'''how to find the count of lower case or upper case in a word or string'''
'''
message = input("Type word: ")


lower_case = sum(1 for c in message if c.islower)
capital_letter = sum(1 for c in message if c.isupper)

print("Lowercase Letters: ", sum(1 for c in message if c.islower)
print("Capital Letters: ", sum(1 for c in message if c.isupper)
print("Total Letters: ", sum(1 for c in message if c.islower and c.isupper))
'''

#not working but I want to be able to combine both of these


'''Exercise 3 - '''

# x="usa, canada, england"
# y=x.split('-')
# print(y)

# a="red sox, patriots, celtics"
# b=a.split(',')
# print(b)


# str = "i cant believe there isnt another movie"
# print(str.replace("nt","ay"))


# str = "thus us a coded message, uvan"
# print(str.replace("u","i"))


'''Exercise 4'''

#attempts to try assign values to letters

'''
{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

def score_string(s):
    return sum([letter_to_numeral[character] for character in s])


score_string('RICE')
'''

import string
mystring = 'ABC'
sum(string.uppercase.index(c) + 1 for c in mystring)








# value ('a') = 1
# value ('b') = 2
# value('c') = 3
# value('d') = 4
# value('e') = 5
# value('f') = 6
# value('g') = 7
# value('h') = 8
# value('i') = 9
# value('j') = 10
# value('k') = 11
# value('l') = 12
# value('m') = 13
# value('n') = 14
# value('o') = 15
# value('p') = 16
# value('q') = 17
# value('r') = 18
# value('s') = 19
# value('t') = 20
# value('u') = 21
# value('v') = 22
# value('w') = 23
# value('x') = 24
# value('y') = 25
# value('z') = 26

''' Exercise 5 '''

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
