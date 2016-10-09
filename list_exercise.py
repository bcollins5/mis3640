# def nested_sum(t):
#     """Computes the total of all numbers in a list of lists.
#     t: list of list of numbers
#     returns: number
#     Expected output:
#     >>> t = [[1, 2], [3], [4, 5, 6]]
#     >>> nested_sum(t)
#     21
#     """


    total = 0 
    for i in t:
        total += sum (i)
    return total









# def cumsum(t):
#     """Computes the cumulative sum of the numbers in t.
#     t: list of numbers
#     returns: list of numbers
#     Expected output:
#     >>> t = [1, 2, 3]
#     >>> cumsum(t)
#     [1, 3, 6]
#     """

#     result = []
#     total = 0
#     for i in t:
#         total += i 
#         result.append(total)
#     return result

    

# def middle(t):
#     """Returns all but the first and last elements of t.
#     t: list
#     returns: new list
#     Expected output:
#     >>> t = [1, 2, 3, 4]
#     >>> middle(t)
#     [2, 3]
#     """


# list = [1,2,3,4,5,6,7]       #present list
# list.pop(0)           #gets rid of first item in list
# #list.pop(1)           #gets rid of second item in list
# list.pop()            #gets rid of last item in list
# print(list)           #prints new list with appropriate adjustments

# *** I get confused on how to START these problems.
# I don't have an approach or a method to start a new program
# I want to be able to know how to go step by step in order to break down a problem

# list = []                      #<-- for example, what follows the definition of a variable?
    # def middle(t):                               #I always see an "for i in t" but does it have to be "t"? what does t represent? it isn't defined or introduced anywhere else 
    # for i in t:        
        # list.pop(0)
        # list.pop()
    # return list             #<--- do I want to return list or t? I don't know what t is








#i wanna to pop out everything but the first and last item in the list

#     result = []
#     first = ([1,], result)   #signals first character in result list
#     last = ([,1], result)    #signals last character in result list
#     for i in t:
#         result.remove(first)
#         result.remove(last)
#     return (t)              #returns t, which has first and last character removed from result list

    
# print( 'new list: ', (result - t))




# def chop(t):
#     """Removes the first and last elements of t.
#     t: list
#     returns: None
#     Expected output:
#     >>> t = [1, 2, 3, 4]
#     >>> chop(t)
#     >>> t
#     [2, 3]
#      """
     #when i put def chop(t) above this code, i need to indent LIST, why??
#def chop(t): --- TypeError: descriptor 'pop' requires a 'list' object but received a 'int'



# list = [1,2,3,4]       #present list
# list.pop(0)           #gets rid of first item in list
# #list.pop(1)           #gets rid of second item in list
# list.pop()            #gets rid of last item in list
# print(list)           #prints new list with appropriate adjustments





# def is_sorted(t):
#     """Checks whether a list is sorted.
#     t: list
#     returns: boolean
#     Expected output:
#     >>> is_sorted([1, 2, 2])
#     True
#     >>> is_sorted(['b', 'a'])
#     False
#     """


# def is_Sorted(lst):
#     if len(lst) == 1:
#        return True
#     return lst[0] <= lst[1] and is_Sorted(lst[1:])

# any_list = [1,2,3,4,4,4,6,7,4]       #False
# print (is_Sorted(any_list))



#information & assistance in the problem above is taken from stackoverflow website

def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """




word_1 = 'newspaper'
word_2 = 'papersnow'

def is_anagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)


print(is_anagram(word_1, word_2))






#information & assistance in the problem above is taken from stackoverflow website





def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    """

    for i in s:
        if s.count(i)>1
            return True

        else:
            return False
    

def has_adjacent_duplicates(s):
    "

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))




# def main():
#     t = [[1, 2], [3], [4, 5, 6]]
#     print(nested_sum(t))

#     t = [1, 2, 3]
#     print(cumsum(t))

#     t = [1, 2, 3, 4]
#     print(middle(t))
#     chop(t)
#     print(t)

#     print(is_sorted([1, 2, 2]))
#     print(is_sorted(['b', 'a']))

#     print(is_anagram('stop', 'pots'))
#     print(is_anagram('different', 'letters'))
#     print(is_anagram([1, 2, 2], [2, 1, 2]))

#     print(has_duplicates('cba'))
#     print(has_duplicates('abba'))


# if __name__ == '__main__':
#     main()