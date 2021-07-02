# 30.Print positive numbers in a list
list = [1, 2, -4, -8, 5, 7, -1]
# a
for i in range(len(list)):
    if list[i] > 0:
        print(list[i], end=",")

# b
i = 0
while i < len(list2):
    if list2[i] > 0:
        print("\n", list2[i], end=" ")
    i += 1

# c
a=filter(lambda x: x > 0, list2)
print("\n",list(a))

# d
positive_numbers = [x for x in list2 if x > 0]
print("Positive numbers are", positive_numbers)