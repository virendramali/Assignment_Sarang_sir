# 43.Python program to print even length words in a string
s = input("Enter string:")
a = s.split()
l = []
for i in a:
    if len(i) % 2 == 0:
        l.append(i)
print("Even length words are:", l)