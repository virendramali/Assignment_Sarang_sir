# 45.Python program to count the Number of matching characters in a pair of string
s1 = input("Enter first string:")
s2 = input("Enter second string:")
a = s1.split()
b = s2.split()
l = []
for i in a:
    for j in b:
        if i == j:
            l.append(i)
print("Number of matching characters in a pair of string are:", len(l))