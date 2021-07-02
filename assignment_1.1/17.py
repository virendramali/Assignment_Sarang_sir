#17.Reversing a list
#a
l=[1, 2, 3, 4, 'a', 'b']
l.reverse()
print(l)

#b
l1=l[::-1]
print(l1)

#c
l2=[]
for i in range((len(l1)-1),-1,-1):
    l2.append(l1[i])
print(l2)