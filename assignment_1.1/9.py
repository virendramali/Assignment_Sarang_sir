# 9.Python Program to Split the array and add the first part to the end.
n = int(input("Enter number:"))
arr = [1, 2, 3, 4, 5, 6, 7]
a = []
for i in range(n, len(arr), 1):
    a.append(arr[i])
a.extend(arr[0:n])
print(a)