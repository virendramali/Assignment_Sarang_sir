# 29.Count even and odd numbers in a list
list1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
even = 0
odd = 0
for i in list1:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers in list are", even)
print("Odd numbers in list are", odd)