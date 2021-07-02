# 52.Python program to find uncommon words from two Strings
# a
s1 = input("Enter first string:")
s2 = input("Enter second string:")
set1 = set(s1.split())
set2 = set(s2.split())
set3 = set1.symmetric_difference(set2)
print("Uncommon words from two string are:", ','.join(set3))


# b
l1 = list(s1.split())
l2 = list(s2.split())
l3 = []
for i in l1:
    if i not in l2:
        l3.append(i)
for j in l2:
    if j not in l1:
        l3.append(j)
print("Uncommon words are:", ','.join(l3))