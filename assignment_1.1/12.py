# 12.Python program to swap two elements in a list
l = [1, 2, 3, 4, 5, 6, 7]
l[0], l[1], l[-2], l[-1] = l[-2], l[-1], l[0], l[1]
# l[-2], l[-1] = l[0],l[1]
print(l)