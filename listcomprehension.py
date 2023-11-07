x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [x*2 for x in x]
print(a)

b=[]
for zahl in x:
    if zahl%2 ==0:
        b.append(zahl)
print(b)


c=[]
for element in y:
    if element is True:
        c.append(element)
print(c)


d=[]
for item in y:
    if isinstance(item, str):
        d.append(item)
print(d)

e=[]
e = [[True] * i for i in x if i % 2 == 1]

print(e)
