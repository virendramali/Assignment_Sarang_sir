l = [3, 4, 2]
# a
mul = 1
for i in range(len(l)):
    mul *= l[i]
print("Multiplication of numbers:", mul)


# b
mul = 1
for i in l:
    mul *= i
print("Multiplication of numbers in list:", mul)