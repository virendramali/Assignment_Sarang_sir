#1.factorial of a number with and without recursion
#with recursion
def recursion(n):
    if n==0:
        print("Enter positive integer number")
    elif n==1:
        return n
    else:
        return n * recursion(n-1)
print(recursion(3))

#without recursion
#a
a=1
for x in range(1,5):
    a *= x
print(a)

#b
i=1
mul=1
while i<=5:
    mul *= i
    i+=1
print(mul)


#2.Check Armstrong number
#a
n=int(input("Enter number:"))
sum=0
order=len(str(n))
i=n
while i>0:
    num = i%10
    sum += num**order
    i//=10
if sum==n:
    print(n,"is armstrong number")
else:
    print(n,"is not armstrong number")


#3.Print all prime numbers in an interval
#a
n=int(input("Enter range:"))
if n>1:
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)


#4.Program for fibonacci numbers
n=int(input("Enter number:"))
a=[]
for i in range(n):
    if i==0:
        a.append(0)
    elif i==1:
        a.append(1)
    else:
        a.append(a[i-2]+a[i-1])
print("Fibonacci numbers are:",end="")
print(a)


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


