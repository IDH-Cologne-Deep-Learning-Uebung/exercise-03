x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = []
b = []
c = []
d = []
e = []

for element in y:
    if type(element) == bool:
        if element:
            c.append(element)
    if type(element) == str:
        d.append(element)

for element in x:
    a.append(element * 2)
    if element % 2 == 0:
        b.append(element)
    if element % 2 != 0:
        temp = []
        int = 0
        while element > int :
            temp.append(True)
            int +=1
        e.append(temp)

print(a,b,c,d,e)