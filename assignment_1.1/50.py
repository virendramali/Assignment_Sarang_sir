# 50.Python program to check if a given string is binary string or not
# a
string = input("Enter string:")
s = {0, 1}
s1 = {x for x in string}
if len(s1) == len(s):
    print(f"'{string}' is binary string.")
else:
    print(f"'{string}' is not binary string.")


# b
string = input("Enter string:")
s = "01"
count = 0
for i in string:
    if i not in s:
        count += 1
        break
    else:
        pass
if count == 1:
    print("Given string is not binary string")
else:
    print("Given string is binary string")
