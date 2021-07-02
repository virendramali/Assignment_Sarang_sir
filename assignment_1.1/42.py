# 42. Python | Check if a Substring is Present in a Given String
# Find length of a string in python (4 ways)

string = input("Enter string:")
sub_string = input("Enter sub string:")
a = string.split()
b = sub_string.split()
count = 0
for i in b:
    if i in a:
        count += 1
    else:
        pass
if len(b) == count:
    print("sub_string is present in string.")
else:
    print("sub_string is not present in string")


#
s = input("Enter string:")
# 1
count = 0
for i in s:
    count += 1
print(count)

# 2
print(len(s))

# 3
from collections import Counter
a = Counter(s)
count = 0
for i in a:
    count += a[i]
print(count)

# 4
from collections import Counter
a = Counter(s)
count = 0
for i in a.values():
    count += i
print(count)