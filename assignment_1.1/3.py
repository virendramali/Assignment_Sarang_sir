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