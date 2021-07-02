# 13.Python program to remove Nth occurrence of the given word
string = input("Enter string:")
letter = input("Enter letter to be removed:")
n = int(input("Occurence of letter:"))
l = [x for x in string]
l2 = []
count = 0
for i in l:
    if i == letter:
        count += 1
        if count != n:
            l2.append(i)
    else:
        l2.append(i)
print(''.join(l2))