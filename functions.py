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

# check the number of arguments. 
# If there are less than two arguments, return a string with the number of arguments. 
# If there are two arguments, pass them to `func1`. 
# If there are more than two arguments, return the number of arguments as an int value. 
def func2(*args):
  if len(args) < 2:
    return str(len(args))
  if len(args) == 2:
    return func1(*args)
  if len(args) > 2:
    return len(args)
    
  

func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)

print(func1(1,2))
print(func1("Welt", "Hallo"))
print(func1(None, None))
print(func1(11, "Freunde"))
print(func1(5.4, 3.6))

print("----")

print(func2(2))
print(func2(2, 3))
print(func2(4, "3"))
print(func2("Goodbye", "World"))
print(func2(2, 3, 3, "test"))