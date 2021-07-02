#5.Find sum of array
list1=[1,2,3,4,5,6]
#a
print(sum(list1))

#b
sum=0
i=len(list1)
while i>0:
    sum+=i
    i-=1
print(sum)

#c
sum=0
for i in list1:
    sum+=i
print(sum)