num1 = float(input("Enter first number:\n"))
num2 = float(input("Enter second number:\n"))

choice = input("Choose opration\n 1. Addition\n 2. Substraction\n 3. Multiplication\n 4. Division\n 5. Square\n 6. Cube\n")

while(True):
    if choice == "1":
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == "2":
        print(num1, "-", num2, "=", num1 - num2)
    
    elif choice == "3":
        print(num1, "x", num2, "=", num1 * num2)
    
    elif choice == "4":
        print(num1, "÷", num2, "=", num1 / num2)

    elif choice == "5":
        print("The square of", num1, "is", num1 * num1)
        print("The square of", num2, "is", num2 * num2)
    
    elif choice == "5":
        print("The cube of", num1, "is", num1 * num1 * num1)
        print("The cube of", num2, "is", num2 * num2 * num2) 
    
    else:
        print("WRONG FORMATE")
        continue
    

  
     


    
