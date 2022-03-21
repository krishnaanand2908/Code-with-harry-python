books = ["Maths", "Science", "Rs Agrwal", "Honeydew", 1000]
print(books[4])
print(books[1])
print(books[3])
print(books[2])

numbers = [1, 3, 4, 6, 7, 9, 10]
print(numbers[2])

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(numbers[1:5])

print(max(numbers))
print(min(numbers))

numbers.append(7)
print(numbers)

numbers.append(7)
numbers.append(7)
numbers.append(7)
numbers.append(7)
print(numbers)

numbers.insert(5, 81)
print(numbers)

numbers.remove(7)
numbers.remove(7)
numbers.remove(7)
numbers.remove(7)
numbers.remove(7)
numbers.remove(7)
print(numbers)

#numbers.pop()
#print(numbers)

numbers[1] = 100
print(numbers)

tp = (20, 25, 10, 105)
print(tp)

#tp cannot be changed

a = 1
b = 2

temp = a
b = temp

print(temp)

c = 4
d = 5

c, d = d, c
print(c ,d)