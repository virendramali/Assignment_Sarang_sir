#14.Find length of list
list1 = ["abc", "pqr", 1, 2, 3, 4, 5]
#a
print(len(list1))

#b
length = 0
for i in list1:
    length += 1
print(length)

#c
i = 1
l = 0
while i <= len(list1):
    l += 1
    i += 1
print(l)


#15.Check if element exists in list
list2=["virendra", "sagar", 12, 13, 14, ["a", "b", "c"]]
#a
def element_check(a):
    if a in list2:
        return True
    else:
        return False
print(element_check("sagar"))

#b
for i in list2:
    if i==14:
        print("Present")


#16.Ways to clear a list
#a
list3=[1, 2, 3, 4]
list3.clear()
print(list3)

#b
list4=[1, 3, 5, 7, 9]
del list4[:]
print(list4)

#c
list5=[5, 6, 7, 8, 9]
for i in range(len(list5)):
    list5.pop()
print(list5)

#d
def abc(list):
    for i in range(len(list)):
        list.pop()

list6=[1,2,3,4]
a=filter(abc(list6),list6)
print(list(a))

#e
list7=["pqr", "lmn"]
b=list(filter(lambda x: x==0, list6))
print(b)


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


#20.Find the sum of elements in list
l=[3, 4, 5, 5, 7, 8, 9]
#a
print(sum(l))

#b
sum=0
for i in l:
    sum+=i
print(sum)