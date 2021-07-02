# 25.Print even numbers in list
l = [1, 2, 3, 4, 5, 6]
# a
for i in l:
    if i % 2 == 0:
        print(i)

# b
l2 = [x for x in l if x % 2 == 0]
print("Even numbers list:", l2)