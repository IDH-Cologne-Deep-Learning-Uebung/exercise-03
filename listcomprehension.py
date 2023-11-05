x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

# Liste aller X-Elemente mit 2 multipliziert
a = []
for number in x:
    a.append(number * 2)
print(a)

# Liste aller graden X-Elemente
b = []
for num in x:
    if num % 2 == 0:
        b.append(num)
print(b)

# Liste aller True-Elemente
c = []
for wahr in y:
    if wahr == True:
        c.append(wahr)
print(c)

# Liste aller String-Elemenete von y
d = []
for string in y:
    if isinstance(string, str):
        d.append(string)
print(d)

# Liste alle ungeraden X_Elementen
e = []
for odd in x:
    if odd % 2 != 0:
        true =[True] * odd
        e.append(true)
print(e)