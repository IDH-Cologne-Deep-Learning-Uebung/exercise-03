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
  args_size = len(args)

  if args_size < 2:
    print('case1')
    return str(args_size)

  elif args_size == 2:
    print('case2')
    func1(args[0],args[1])

  elif args_size > 2 :
    print('case3')
    return args_size

func2(2)
func2(2,3)
func2(2,4,4)
func2(2,23,3,4,4,4,4)

def func3(*args, **kwargs):
  args_size = len(args)

  if args_size < 2:
    keylist = []
    valuelist = []

    for key, value in kwargs.items():
      keylist += ({key})
      valuelist += ({value})
    print(keylist,valuelist)

    if keylist.count("a") == 1 and keylist.count("b") == 1:
      func1(valuelist[0], valuelist[1])
      print('a and b')

    else:
      print('else')
      func2(valuelist[0], valuelist[1])

func3(a=3,b=4)
func3(a=3, c=3)