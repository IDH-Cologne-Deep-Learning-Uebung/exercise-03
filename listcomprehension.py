x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = []
for zahl in x:
    a.append(zahl * 2)

print(a)

b = []
for zahl in x:
    if zahl % 2 == 0:
        b.append(zahl)

print(b)

c = []
for element in y:
    if element:
        c.append(element)
print(c)

d = []
for element in y:
    if type(element) == str:
        d.append(element)
print(d)

e = []
for zahl in x:
    if zahl % 2 == 0:
        list = []
        for x in range(zahl):
            list.append(True)
        e.append(list)
print(e)

