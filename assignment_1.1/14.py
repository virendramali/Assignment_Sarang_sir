#14.Find length of list
list1 = ["abc", "pqr", 1, 2, 3, 4, 5]
#a
print(len(list1))

#b
length = 0
for i in list1:
    length += 1
print(length)

#c
i = 1
l = 0
while i <= len(list1):
    l += 1
    i += 1
print(l)