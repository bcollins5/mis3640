grades = {'Jerry': 75, 'Rose': 95}
print(grades['Jerry'])

grades['Brian'] = 90
print(grades)

print(len(grades))
print('Jerry' in grades)
print(90 in grades.values())



def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


    