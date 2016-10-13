
def replace_even(data):
    '''
    Replace all elements at an even index in the list with 0.
    No return is required.
    data: the list of values to process'''
    for i in range(len(ONE_TEN)):
        if i % 2 == 0:
            ONE_TEN[i]=0      #supposed to append the number if it has no remainders when
                              #divided by 2 (AKA even #)


    # pass

# # Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
replace_even(ONE_TEN)
print(ONE_TEN)


def remove_middle(data):
    '''
    Remove the middle element if the list length is odd,
    or the middle two elements if the list length is even.  
    No return is required.
    data: the list of values to process
    '''




    if len(data) % 2 == 0:
        data.pop(len(data)// 2)    # // 2-1 also works
        data.pop(len(data)// 2)
    else:
        data.pop(len(data)// 2)


    #     ONE_TEN.remove('middle_integer')
    # else
    #     ONE_TEN.remove('middle_two_integers')
    # pass



# Uncomment the following lines to test
# middle_integer = midddle.ONE_TEN
# middle_two_integers = ("figure out calculation")
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove_middle(ONE_TEN)
print(ONE_TEN)


def insert_integer(data, number):     #i don't know how to communicate the variables up here, to down in the rest of the fuction
    '''                               #i need to actually learn how to even start / create these functions

    given a sorted list of integers, insert a new integer into
    its proper position so that the new list stays sorted. 
    Do not use sort function or sorted function inside this function.
    data: a list of integers
    number: a new integer
    return: a new list of sorted integers with previous numbers and 
    the new number
    '''
#before we insert dat its a serach problem

    for i in range(len(data)):
        if data[i] > number:
            data.insert(i, number)
            break
    return data



# import bisect
# data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
# bisect.insort(data, 2015)          #use bisect function to insert in proper location
# print(data)

# Uncomment the following lines to test
data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
new_data = insert_integer(data, 2015)
print(new_data)


def print_hist(data):
    '''
    given a dictionary of letter: positive integer pairs, 
    print rows with the letter and a number of asterisks equal
    to the positive integer. The rows should be printed in key order.
    No return is required.
    data: a dictionary of letter: positive integer pairs
    Example:
    letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
    print_hist(letter_counts)
    Expected output:
    A: ***
    B: **********
    C: ******
    Z: ********
    '''
    pass



    key_list = data.keys()
    print('For testing key list', key_list)
    key_list.sort()
    print('For testing key list after sorting',)