# 21.Multiply all numbers in list
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


# 22.Find smallest number in list
l1 = [23, 45, 67, 12, 4]
# a
print("Smallest number in list:", min(l1))

# b
def smallest(l):
    l.sort()
    print("Smallest number in list:", end="")
    print(l[0])
smallest(l1)


# 23.Find largest number in list
l2 = [12, 45, 3, 266, 100]
# a
print("Largest number in list is", max(l2))

# b
def largest(l):
    l.sort()
    return l[-1]
print("largest number in list:", end="")
print(largest(l2))


# 24.Find second largest number in list
l3 = [3, 24, 14, 6, 50]
l3.sort()
print("Second largest number in list is", l3[-2])


# 25.Print even numbers in list
l4 = [1, 2, 3, 4, 5, 6]
# a
for i in l4:
    if i % 2 == 0:
        print(i)

# b
l5 = [x for x in l4 if x % 2 == 0]
print("Even numbers list:", l5)

# 26.Print odd numbers in list
# a
for i in l4:
    if i % 2 != 0:
        print(i)

# b
a = filter(lambda x: x % 2 != 0, l4)
print(a)
print(list(a))


# 27.Print all even numbers in range
# a
n = int(input("Enter range:"))
for i in range(n+1):
    if i % 2 == 0:
        print(i)

# b
i = 0
n=10
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1


# 28.Print all odd numbers in range
# a
for i in range(0, 10, 1):
    if i % 2 != 0:
        print(i)

# b
i = 0
n=10
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1


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


# 30.Print positive numbers in a list
list2 = [1, 2, -4, -8, 5, 7, -1]
# a
for i in range(len(list2)):
    if list2[i] > 0:
        print(list2[i], end=",")

# b
i = 0
while i < len(list2):
    if list2[i] > 0:
        print("\n", list2[i], end=" ")
    i += 1


# b
a=filter(lambda x: x > 0, list2)
print("\n", list(a))

# c
positive_numbers = [x for x in list2 if x > 0]
print("Positive numbers are", positive_numbers)



