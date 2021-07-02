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