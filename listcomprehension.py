x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [z*2 for z in x] # oder statt z x?
print(a)
b = [z for z in x if z%2 == 0]
print(b)
c = [z for z in y if z == True]
print(c)
d = [z for z in y if isinstance(z, str)]
print(d)

def convert(zahl):
    liste = []
    i = zahl
    while i > 0:
        liste.append(True)
        i = i - 1
    return liste

e = []
i = 0
for z in x:
    if z%2 == 1:
        e.append([])
        e[i].append(convert(z))
        i = i + 1
print(e)

