# 7.Program for array rotation
arr = [1, 2, 8, 5, 10, 34, 20]
# a
n = int(input("Enter number for rotation:"))
a = arr[n:len(arr)] + arr[0:n]
print("Array rotation using slicing:", a)

# b
n = int(input("enter no:"))
a = []
for i in range(n, len(arr)):
    a.append(arr[i])
a += arr[0:n]
print("Array rotation using for loop:", a)