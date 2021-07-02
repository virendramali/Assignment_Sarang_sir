# 23.Find largest number in list
l = [12, 45, 3, 266, 100]
# a
print("Largest number in list is", max(l))

# b
def largest(l):
    l.sort()
    return l[-1]
print("largest number in list:", end="")
print(largest(l))