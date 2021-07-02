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