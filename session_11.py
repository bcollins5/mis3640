#Exercise 4
#Problem 1

'''Write a function that reads the words in words.txt and 
stores them as keys in a dictionary. It doesn’t matter 
what the values are. Then you can use the in operator as 
a fast way to check whether a string is in the dictionary.'''


# list = [word.txt]

# import os
# os.chdir("C:/Users/bcollins5/Documents/GitHub/mini-project-hangman-bcollins5/words.txt")
# fname = input("File name: ")
# if len(fname) < 1 : fname = "words.txt"
# fh = open(fname)
# counter = 0
# dictionary = dict()
# for line in fh:
#     word = line.rstrip().split()
#     for word in words:
#         dictionary[word] = counter
#         counter += 1

# print(dictionary)



#resources used/information collected from the following:
#daniweb.com , stackoverflow


#Problem 2
'''Write a function named has_duplicates that takes
a list as a parameter and returns True if there is 
any object that appears more than once in the list.'''


list_of_SB_winner_in_last_five = ['Broncos', 'Patriots', 'Seahawks', 'Ravens', 'Giants']

def has_duplicate(myList):
     dictionary = {}
     for word in myList:
        dictionary[word] = 1 + dictionary.get(word, 0)
        if dictionary[word] > 1:        #there is an issue within the lines above, where it is not
            return True                 #correctly counting duplicates (maybe something to do with 'dictionary')
        else:
            return False

print(has_duplicate(list_of_SB_winner_in_last_five))

list_of_WS_winner_in_last_five = ['Royals' 'Giants', 'Red Sox', 'Giants', 'Cardinals']

print(has_duplicate(list_of_WS_winner_in_last_five))



### help / issue to fix: it is not returning True for List of WS winners, when Giants is there twice
##resources used/information collected from the following:
#thinkpy-solutions, stackoverflow

