# 48.Python program for removing i-th character from a string
s = input("Enter string:")
i = int(input("Enter position of character to be removed:"))
l = [x for x in s]
for y in range(len(l)):
    if y == i-1:
        l.remove(l[i-1])
print(l)

