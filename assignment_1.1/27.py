# 27.Print all even numbers in range
# a
n = int(input("Enter range:"))
for i in range(n+1):
    if i % 2 == 0:
        print(i)

# b
i = 0
n=10
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1