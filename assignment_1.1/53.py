# 53.Python program to swap commas and dots in a String
# a
s = input("Enter string:")
l = [x for x in s]
l1 = []
for ele in l:
    if ele == ".":
        l1.append(",")
    elif ele == ",":
        l1.append(".")
    else:
        l1.append(ele)
print(''.join(l1))

# b
s1 = s.replace(".", "!")
s1 = s1.replace(",", ".")
s1 = s1.replace("!", ",")
print(s1)

