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

##Testing
func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)

def func (** kwargs ):
 # inside the function , kwargs = dictionary
  for key in kwargs :
    print ( key + ": " + str ( kwargs [ key ]))
  return

def func2 (*args):
  print(len(args))

  if(len(args) < 2):
    return str(len(args))
  print(func2('Hallo'))

  if (len(args) == 2):
    return func1(args[0], args[1])    

  if (len(args) > 2):
          return len(args)


def func1(a, b):
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
  print(f"func1: a={a}, b={b}")

def func2(**kwargs):
  def func2 (*args):
    print(len(args))

  if(len(args) < 2):
    return str(len(args))
  print(func2('Hallo'))

  if (len(args) == 2):
    return func1(args[0], args[1])    

  if (len(args) > 2):
          return len(args)

  print(f"func2: {kwargs}")

def func3(**kwargs):
    # Check if 'a' and 'b' are there
    if 'a' in kwargs and 'b' in kwargs:
        # If both! 'a' and 'b' are there, pass to func1
        func1(kwargs['a'], kwargs['b'])
    else:
        # If 'a' and 'b' are not both there, pass all arguments to func2
        func2(**kwargs)

# Example usage:
func3(a=1, b=2, c=3, d=4)


# Testing
print('1. : Anzahl der Arguemte anzeigen: ' + func2("Hallo"))
print('2. : Unter 2 Args, int erwartet: ')
print(func2(1, 2))
print('3. : >2 Args, give Anzahl as int: ' + str(func2(1, 2, 3)))