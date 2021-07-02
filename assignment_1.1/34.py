# 34.Count positive and negative numbers in list
list1 = [1, -1, 2, -2, 3, -3, 4]
positive_num = 0
negative_num = 0
for i in list1:
    if i < 0:
        negative_num += 1
    else:
        positive_num += 1
print("\nPositive numbers:", positive_num)
print("Negative numbers:", negative_num)