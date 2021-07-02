# 22.Find smallest number in list
l = [23, 45, 67, 12, 4]
# a
print("Smallest number in list:", min(l))

# b
def smallest(l):
    l.sort()
    print("Smallest number in list:", end="")
    print(l[0])
smallest(l)