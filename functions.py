def func1(a, b):
  if type(a) == int and type(b) == int:
    return a+b
  if type(a) == str and type(b) == str:
    return b+" "+a
  if a is None and b is None:
    return "Does not exist."
  if type(a) != type(b):
    return None
  return type(a)


func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)


def func2(*args):
  #print(args)
  if len(args) < 2:
    return str(len(args))
  if len(args) == 2:
    func1(args[0], args[1])
  if len(args) > 2: 
    return int(len(args))
  
#print(func2(1,2,7))

def func3(**kwargs ):
  a=None
  b=None
  l = []

  for key in kwargs:
    if key == "a":
      a = kwargs[key]
      #print(str(kwargs[key]))
    if key == "b":
      b = kwargs[key]
      #print(str(kwargs[key]))
  
    l.append(key)

  if a != None and b != None:
    func1(a,b)
  else:
    func2(*l) #unpack objects
    #print(l)
    #print(func2(*l))

#print(func3(c=3,a=5,x=1, d=2))
#print(func3(c=3,a=5,x=1, b=4))
#print(func1(5,4))



#-> wegen der nicht vorhandenen Ausgabe von return, 
# wäre print doch sinnvoller (teilweise) (für diese aufgabe)?
