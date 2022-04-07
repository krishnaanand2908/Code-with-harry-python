def function1(a, b):
    print("This is function 1")
    
def function2(a, b):
    power = (a ** b)
    return power
a = function1(2, 3)
b = function2(2, 3)

print(a)
print(b)

def function3(c, d):
    """This is a docstring"""
    
print(function3.__doc__)