# 35.Remove multiple elements from list
list = ["abc", "pqr", 1, 2, 3, 4]

def abc(l):
    for i in list:
        for j in l:
            if j in list:
                list.remove(j)
        return list
a = abc([1, 2])
print(a)