choice = input("Choose one:\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n")
num1 = float(input("Enter the first number:\n"))
num2 = float(input("Enter the second number:\n"))

if choice == "1":
    print(num1,"+", num2, "=", num1 + num2)
    
elif choice == "2":
    print(num1,"-", num2, "=", num1 - num2)
    
elif choice == "3":
    print(num1,"x", num2, "=", num1 * num2)
    
elif choice == "4":
    print(num1,"÷", num2, "=", num1 / num2)
    
else:
    print("Wrong Formate")