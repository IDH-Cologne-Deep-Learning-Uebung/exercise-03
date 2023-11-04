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

# `func2` takes an arbitrary number of arguments. 
#  The function checks the number of arguments.
#  If there are less than two arguments, it returns a string with the number of arguments.
#  If there are two arguments, it passes them to `func1`. 
#  If there are more than two arguments, it returns the number of arguments as an int value. 
def func2(*a):
  if len(a) < 2:
    return str(len(a))
  if len(a) == 2:
    return func1(a[0],a[1])
  if len(a) > 2:
    return int(len(a))
   
# `func3` takes an arbitrary number of named arguments.
#  The function checks that two of these arguments have the names `a` and `b`. 
#  If so, it passes them into `func1`. If not, all names of the arguments are passed into `func2`.
def func3(**a):
  if 'a' in a and 'b' in a:
    return func2(a['a'],a['b'])
  else:
    return func2(a)

print(func3(a="1", b="2", c="3"))
print(func3(say="Hello", ask="World"))
print(func3(x="Hello", a=6, z=5, b=2))
print("END")

print(func2(1))
print(func2("Welt", "Hallo"))
print(func2(None, None))
print(func2(11, "Freunde", "Hallo"))
print(func2(5.4, 5, 3.6))

# print(func1(1,2))
# print(func1("Welt", "Hallo"))
# print(func1(None, None))
# print(func1(11, "Freunde"))
# print(func1(5.4, 3.6))


