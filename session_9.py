'''

Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that 
sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i.
 If you could take out those i’s it would work. 
 But there is a word that has three consecutive pairs of 
 letters and to the best of my knowledge this may be the only word.
 Of course there are probably 500 more but I can only think of one. 
 What is the word? 

 '''


def equal_triple_double(word):

     i = 0
     count = 0
     while i < len(word) - 1:
         if word[i] == word [i + 1]:
             count = count + 1
             if count == 3:
                 return True
             i = i + 2
         else:
             count = 0
             i = i + 1
     return False




def find_triple_double():

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if equal_triple_double(word):
            print(word)



print("3 consecutive double letter words: ")

find_triple_double()