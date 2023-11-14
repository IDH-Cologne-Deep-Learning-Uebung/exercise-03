x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [x*2 for x in x]
print(a)

b = [x for x in x if x % 2 == 0] 
print(b)

c = [x for x in y if x == True]
print(c)

# A list called `d` that contains all string elements of `y`
d =[x for x in y if isinstance (x, str)]
print(d)

e = [[True]* var for var in x if var % 2 == 1]
print(e)
