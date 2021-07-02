# 8.Reversal algorithm for array rotation
# a
n = int(input("Enter no.:"))
b = arr[-n:] + arr[0:-n]
print("Reverse array rotation using slicing:", b)

# b
n = int(input("enter no:"))
a = []
for i in range(-n, len(arr)-n):
    a.append(arr[i])
print("Reverse array rotation using for loop:", a)