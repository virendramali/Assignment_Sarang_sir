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