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