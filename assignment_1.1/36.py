# 36.Remove empty tuples from list
list3 = [(),1, 2, (4, 5), ()]
for i in list3:
    if i == ():
        list3.remove(())
print(list3)