x = [0,1,2,3,4,5,6,7,8,9]
print (x)
y = [True, False, False, True, "False", False, True, True, True, "True"]
print (y)
#A list called a that contains all elements of x, multiplied by 2.
a = [x*2 for x in x]
print (a)
#A list called b that contains all even elements of x.
b = [x for x in x if x % 2 == 0 ]
print (b)
#A list called c that contains all truish elements of y
#(i.e., all elements that evaluate to True in a boolean context)
c = [y for y in y if y == True]
print (c)
#A list called d that contains all string elements of y
d = [y for y in y if isinstance(y, str)]
print (d)
#A list called e that contains a list for each odd element of x. 
e = [[True] * x for x in x if x % 2 != 0]
print (e)
#The number of list elements is given by the current number of x,
# and all inner list elements are True.
# Use I.e., the list e starts like this: [[True], [True, True, True], [True, True, True, True, True], ...]

