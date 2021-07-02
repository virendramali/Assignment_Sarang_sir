# 31.Print negative numbers in a list
l1 = [1, 2, -4, -3, 3, -2, -1]
# a
l = []
for i in l1:
    if i < 0:
        l.append(i)
print("Negative numbers are:", l)

# b
a = filter(lambda x: x < 0, l1)
print("Negative number list:", list(a))

# c
l = [i for i in l1 if i < 0]
print("Negative numbers using list comprehension:", l)