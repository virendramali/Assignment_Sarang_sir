#18.Cloning or copying a list
#a
l=["abc", "pqr", "rst", 12, 14]
l2=l.copy()
print(l2)

#b
l3=[]
for i in range(len(l2)):
    l3.append(l2[i])
print(l3)

#c
l4=list(l3)
print(l4)