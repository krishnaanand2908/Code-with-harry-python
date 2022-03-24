from re import S


s = set()
print(type(s))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#s2 = set(a)
#print(type(a))
#print(type(s2))
s.add(1)
print(s)
s.add(2)
print(s)
s.add(1)
print(s)
#therefore set prints unique values.
#set didn't stores same values, charecters, float decimle numbers or integers.

s2 = 42
print(s2)
s.union({1, 2})
print(s)
s.union({1, 2, 3})
print(s)
s1 = s.union({1, 2, 3})
print(s, s1)
s1 = s.intersection({1, 2, 3})
print(s1)

s.remove(1)
print(s)

s1 = {1, 1, 1, 1, 1, 1}
print(s.isdisjoint(s1))