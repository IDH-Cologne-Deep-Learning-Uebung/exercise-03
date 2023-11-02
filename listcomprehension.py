x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

#nr 1 
a = [j * 2  for j in x ]
print(a)

b = [j for j in x if (j % 2) == 0 ]
print(b)


c = [j for j in y if j]
print(c)


d = [j for j in y if isinstance(j, str)]
print(d)


e = [ [ True for s in range(j)] for j in x if j % 2 != 0 ]

print(e)
