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
  numArgs = len(args)
  if numArgs < 2:
    print(str(numArgs))
    return str(numArgs)
  elif numArgs == 2:
    func1(args[0],args[1])
  else:
    print(int(numArgs))
    return int(numArgs)
func2(2)
func2("Welt", "Hallo")
func2(None, None)
func2(11, "Freunde")
func2(5.4, 3.6, 3)


def func3(*kwargs):
  keyisA = False
  keyIsB = False
  for key in kwargs:
    if key == a:
      keyIsA = True
    if key == b:
      keyIsB = True
  if keyIsA and keyIsB:
    func1(kwargs[a],kwargs[b])
  else:
    func2(kwargs)
func3(a=1, b="Hallo", c=0, d=True)
