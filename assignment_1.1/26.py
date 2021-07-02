# 26.Print odd numbers in list
l = [1, 2, 3, 4, 5, 6]
# a
for i in l:
    if i % 2 != 0:
        print(i)

# b
a = filter(lambda x: x % 2 != 0, l)
print(a)
print(list(a))