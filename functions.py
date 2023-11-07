def func1(a, b):
  if type(a) == int and type(b) == int:
    print (a+b)
    return a+b
  if type(a) == str and type(b) == str:
    print(b+" "+a)
    return b+" "+a
  if a is None and b is None:
    print("Does not exist.")
    return "Does not exist."
  if type(a) != type(b):
    print(None)
    return None
  return type(a)

def func2(*args):
  numArgs = len(args)
  if numArgs < 2:
    print(str(numArgs) + " arguments were given.")
    return
  if numArgs > 2:
    print(int(numArgs))
    return 
  if numArgs == 2:
    func1(*args)

def func3(**kwargs):
  if 'a' in kwargs and 'b' in kwargs:
    func1(kwargs['a'], kwargs['b'])
  else:
    func2(*kwargs)

  return

func3(e=1, z=7, c=7, y=4)

func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)