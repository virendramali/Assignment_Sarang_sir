# 46. Python program to count number of vowels using sets in given string
# Remove all duplicates from a given string in Python.

s = input("Enter string:")
v = ["a", "e", "i", "o", "u"]
str_list = [x for x in s]
l1 = []
for i in str_list:
    for j in v:
        if i == j:
            l1.append(i)
        else:
            pass
print("Total number of vowels in given string are:", len(l1))

l2 = []
for x in str_list:
    if str_list.count(x) > 1:
        continue
    else:
        l2.append(x)

print("String after removing duplicates:", ''.join(l2))
