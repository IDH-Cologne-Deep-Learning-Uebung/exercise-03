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

print("ab hier Func2-Ausgabe")

def func2(*arguments):
  numArgs = len (arguments)
  
  if numArgs < 2:
    return str(numArgs)
  if numArgs == 2:
   return func1(arguments[0],arguments[1])
  if numArgs > 2:
    return int(numArgs)

print(func2("Welt", 3, 6))
print(func2(1))
print(func2(1,4,5,6,3))
print(func2(3,4))
print(func2("test", "toller test"))
print("func2 ende")


"""""
def func3(*argumente):
  print(argumente)
  
  #if argumente == 'a' and argumente == 'b':
  if 'a' in argumente and 'b' in argumente:
    return func1(argumente['a'],argumente['b'])
  else:
    return func2(argumente)
    
print("ab hier func3")

print(func3("a","b","c"))
print(func3("hej", "Jag talar svenska"))
print(func3("hi",6,5,6))

"""
def func3(**argumente):
    print(argumente)
    
    if 'a' in argumente and 'b' in argumente:
        return func1(argumente['a'], argumente['b'])
    else:
        return func2(argumente)

# Beispielaufrufe
print("ab hier func3")
print(func3(a="a", b="b", c="c"))
print(func3(foo="hej", bar="Jag talar svenska"))
print(func3(x="hi", y=6, z=5, w=6))
