num1 = input("Enter num 1:\n")
num2 = input("Enter num 2:\n")

try:
    print(num1, "+", num2, "=", int(num1) + int(num2))
except Exception as e:
    print(e)
    
print("PRINT ME NOW!")

           