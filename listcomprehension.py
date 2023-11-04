x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

# A list called `a` that contains all elements of `x`, multiplied by 2.
a = [el*2 for el in x]
print(a)

# A list called `b` that contains all even elements of `x`.
b = [el for el in x if el % 2 == 0]
print(b)

# A list called `c` that contains all truish elements of `y` (i.e., all elements that evaluate to `True` in a boolean context)
c = [el for el in y if el == True]
print(c)

# A list called `d` that contains all string elements of `y`
d = [el for el in y if type(el) == str]
print(d)

# A list called `e` that contains a list for each odd element of `x`. 
# The number of list elements is given by the current number of `x`, 
# and all inner list elements are `True`.
e = [[True for el in range(x[el])] for el in x if y[el] == True]
print(e)