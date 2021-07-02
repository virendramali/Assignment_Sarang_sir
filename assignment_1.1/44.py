# 44.Python program to accept the strings which contains all vowels

s = input("Enter string:")
a = set(s.lower())
v = {"a", "e", "i", "o", "u"}
b = set({})
for i in a:
    if i in v:
        b.add(i)
if len(b) == len(v):
    print("Given string contains all vowels")
else:
    print("Given string not contains all vowels")

