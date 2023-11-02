x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

#- A list called `a` that contains all elements of `x`, multiplied by 2.

a=[zahl*2 for zahl in x]
print(a)

#- A list called `b` that contains all even elements of `x`.
b=[zahl for zahl in x if zahl%2==0]
print(b)

#- A list called `c` that contains all truish elements of `y` (i.e., all elements that evaluate to `True` in a boolean context)
c=[value for value in y if value==True]
print(c)


#- A list called `d` that contains all string elements of `y`
d=[value for value in y if type(value)==str]
print(d)

#- A list called `e` that contains a list for each odd element of `x`. The number of list elements is given by the current number of `x`, and all inner list elements are `True`. Use I.e., the list `e` starts like this: `[[True], [True, True, True], [True, True, True, True, True], ...]`

"""
erster Ansatz hat nicht funktioniert
    e=[]
    e_odd=[zahl for zahl in x if zahl%2!=0]
    print("e_odd: ")
    print(e_odd)

    e=[value for value in e_odd]

    

zweiter Ansatz
    e=[]
    #in e kommt eine liste, die für jedes ungerade Element von X eine liste enthält. Die Anzahl der Listenelemte wird durch die aktuelle Nummer von X vorgegeben. Die Inneren Listelemente sind True
    #1= True
    #3 = True, True, True

    e=[value for value in x ]
"""

"""
e = [[True] * (2 * i + 1) for i in x]
print(e)
#pass klappt nicht, nach der 9 wird einfach weiter gemacht und es werden 11 Trues ausgegeben
"""
#e = [for element in x if element%2!=1 ] 

#e = [[s for s in range(element for element in x if element % 2 == 0)]]
e = [[True]*element for element in x if element %2 ==1]

print(e)