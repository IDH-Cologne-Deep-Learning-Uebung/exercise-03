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

print(func1(1,2))
print(func1("Welt", "Hallo"))
print(func1(None, None))
print(func1(11, "Freunde"))
print(func1(5.4, 3.6))

def func2(*args):
  numArgs = len(args)
  if numArgs < 2:
    return str(args[0]) + ' ' + str(args[1])
  if numArgs == 2:
    func1(*args)
  if numArgs > 2:
    return numArgs
  
def func3(*args):
  test = ""
  for arg in args:
    if arg == "a":
      test + "a"
    if arg == "b":
      test + "b"
  if test == "ab" or test == "ba":
    func1("a", "b")
  else:
    func2(args)