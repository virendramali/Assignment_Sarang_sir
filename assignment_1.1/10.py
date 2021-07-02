# 10.Python program to find reminder of array multiplication divided by n
array = [2, 3, 5, 7, 4]
mul = 1
for i in array:
    mul *= i
print("Multiplication of array:", mul)
n = int(input("Value of n:"))
print("Reminder after division by n:", mul%n)