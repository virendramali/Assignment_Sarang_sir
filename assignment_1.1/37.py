# 37.Print duplicates from a list of integers
l = [1, 2, 3, 1, 1, 4, 4, 3]
# a(Using for loop)
l1 = []
for i in l:
    if l.count(i) > 1 and i not in l1:
        l1.append(i)
print(l1)

# b(Using counter)
from collections import Counter
a = Counter(l)
b = list([x for x in a if a[x]>1])
print(b)