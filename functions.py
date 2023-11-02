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


def func2(*arg):
  argLen= len(arg)

  if argLen< 2:
    return str(len(arg))
  
  if argLen == 2 :
    return func1(arg[0], arg[1])
  
  if argLen > 2:
    return int(len(arg))


  
  return None




def func3(*args ):
  a= None
  b= None
  
  for arg in args:
    if arg == 'a':
      a= arg
    if arg == 'b':
      b = arg
  
  if a is not None and b is not None:
    
    return func1(a, b)


  return func2(args)


#Next, write a function `func3` that takes an arbitrary number of named arguments. Check that two of these arguments have the names `a` and `b`. If so, pass them into `func1`. If not, pass all names of the arguments into `func2`.

#If you haven't figured it out by now: These functions don't make sense, they are just exercise material.



print(func3("a","b"))
