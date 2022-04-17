# f = open("lol.txt", "w")
# a = f.write("Krishna is the best\n")
# f.close
# print(a)

# you can create new file by using open("name.txt", "w")

# f = open("lol.txt", "a")
# a = f.write("Krishna is the best\n")
# f.close
# print(a)

# Handle read and write both

f = open("lol.txt", "r+")
print(f.read())
f.write("THANK YOU")
