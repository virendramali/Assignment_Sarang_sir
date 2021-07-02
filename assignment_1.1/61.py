# 61.Python program to find the sum of all items in a dictionary
d = {"a": 1, "b": 2, "c": 3, "d": 4}

# a
sum = 0
for i in d.values():
    sum += i
print("Sum of all items in a dictionary =", sum)

# b
sum = 0
for i in d:
    sum += d[i]
print("Sum of items:", sum)