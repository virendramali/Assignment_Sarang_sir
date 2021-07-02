# 32.Print all positive numbers in range
print("Positive numbers in range are:", end="")
for i in range(-10, 10):
    if i > 0:
        print(i, end=",")

# b
i = -5
while i < 5:
    if i > 0:
        print("\n",i, end="")
    i += 1