#19.Count occurrences of an element in list
l=[1, 2, 1, 1, 2, 3, 4, 5]
#a
n=int(input("Enter any number from list:"))
print(f"{n} occurs",l.count(n),"times in list.")

#b
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)