age = int(input("Enter your age here:\n"))

if age == 18:
    print("We can't say that wethere you are eligible for getting a driving lisence or not. You should come to our office and give a physical test for getting a driving lisence")

elif age < 18 or age > 100:
    print("You are not eligible for getting a driving lisence.")
    
elif age > 18 or age < 101:
    print("You are eligible for getting a driving lisence.")
    
else:
    print("ERROR")