x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

#all elements of `x`, multiplied by 2.
a = [i*2 for i in x]                    
print("list a: " + ", ".join(str(num) for num in a))
#all even elements of `x`.
b = [i for i in x if(i%2==0)]           
print("list b: " + ", ".join(str(num) for num in b))
#all truish elements of `y` (i.e., all elements that evaluate to `True` in a boolean context)
c = [i for i in y if(i == True)]        
print("list c: " + ", ".join(str(i) for i in c))
#all string elements of `y`
d = [i for i in y if(type(i) == str)]   
print("list d: " + ", ".join(d) )
#a list for each odd element of `x`. The number of list elements is given by the current number of `x`, and all inner list elements are `True`. Use I.e., the list `e` starts like this: `[[], [True, True], [True, True, True, True], ...]`
e = [ [True]*x.index(i) for i in x if(i%2 == 0)]         
print("list e: " + ", ".join(str(num) for num in e))
