# 11.Python program to interchange first and last element in list
l = [1, 2, 3, 4, 5, 6]
l[0], l[-1] = l[-1], l[0]
print(l)