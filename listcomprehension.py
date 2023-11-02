x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]



a = [z*2 for z in x ]
print(a)
b = [z for z in x if (z%2==0)]
print(b)

c = [b for b in y if b] #==True funktioniert nicht!, nur die variable ist am besten
print(c)

d = [s for s in y if type(s) == str ]
print(d)
e = [ [True for t in range(l)]  for l in x if (l%2!=0)]
print(e)




#e, nur ohne list comprehension

#f = []
#p=0
#for l in x:
#    if (l%2!=0):
#        f.append([])
#        for k in range(l):
#            f[p].append(True)
#        p=p+1
#print(f)
