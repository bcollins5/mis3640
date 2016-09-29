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


str = "i cant believe there isnt another movie"
print(str.replace("nt","ay"))


str = "thus us a coded message, uvan"
print(str.replace("u","i"))




