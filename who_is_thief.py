"""
Four suspects; one of them is a thief. In interrogation
    John said: I am not the thief.
    Paul said: George is the thief.
    George said: It must be Ringo.
    Ringo said: George is lying.
Among them, three were telling the truth while one was lying.
Could you find out who is the thief?
"""


for thief in ['John', 'Paul', 'George','Ringo']:
    sum = (thief != 'John') + (thief == 'George') + \
        (thief == 'Ringo') + (thief != 'Ringo')
    if sum == 3:
        print('The thief is {}.'.format(thief))



    #if John, Paul, George = True, then Ringo = False (LIAR)
    #if John, Paul, Ringo = True , then George = False (LIAR)

# "John" ! = thief
# "George" == thief
# "Ringo" == thief
# "Ringo" != thief

