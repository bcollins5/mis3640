grades = {'Jerry': 75, 'Rose': 95}
print(grades['Jerry'])

grades['Brian'] = 90
# grades['Cole'] = 100
# print(grades)

# print(len(grades))
# print('Jerry' in grades)    #returns TRUE if Jerry is in grades list
# print(90 in grades.values())  #returns TRUE if there is a 90



def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('Bookkeeper')
# print(histogram('Book'))

number_of_e = h.get('a', 0)
print(number_of_e)


def print_hist(h):
    for c in h:
        print(c, h[c])

# h = histogram('assachusetts')
# print_hist(h)

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

h = histogram('Massachusetts')
key = reverse_lookup(h, 2)
print(key)