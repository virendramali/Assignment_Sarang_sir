#15.Check if element exists in list
list2=["virendra", "sagar", 12, 13, 14, ["a", "b", "c"]]
#a
def element_check(a):
    if a in list2:
        return True
    else:
        return False
print(element_check("sagar"))

#b
for i in list2:
    if i==14:
        print("Present")