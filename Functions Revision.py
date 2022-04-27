# a = 10
# b = 12
# c = sum((a, b)) #built in functions
# print(c)

# def function1():
#     print("Hello you are in function1")
    
# print(function1())
# function1()
# num1 = int(input("Enter a number here:\n"))
# num2 = int(input("Enter another number here:\n"))

# def sum1():
#     a = (num1 + num2)
#     print(a)
#     return a
    
    
# a = sum1()
# print(a)
x = int(input("Define x as an integer:\n"))
y = int(input("Define y as an integer:\n"))
opr = input("Choose your operation:\n + for addition\n - for substraction\n x for multiplication\n / for division\n")
def algebra():
    """This function can be used as a calculator"""
    """This function cannot be used for two numbers"""
    if opr == "+":
        solve = x + y
    elif opr == "-":
        solve = x - y
    elif opr == "x":
        solve = x * y
    elif opr == "/":
        solve = x / y
    else:
        solve = "Thenga"
        
    print(solve)
    return solve
algebra()
print(algebra.__doc__)