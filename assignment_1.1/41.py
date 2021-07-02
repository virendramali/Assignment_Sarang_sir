# 41.Python Ways to remove i’th character from string
# a
string = input("Enter string:")
n = int(input("Enter value of i:"))
l = [y for y in string]
del(l[n-1])
print(''.join(l))

# b
l1 = [x for x in string]
l1.remove(l1[n-1])
print(''.join(l1))

# c
l2 = [i for i in string]
for x in range(len(l2)):
    if n == x+1:
        del(l2[n-1])
print(''.join(l2))
