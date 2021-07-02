# 67.Python to remove all duplicate words from a given sentence
# a
sentence = input("Enter a sentence:")
l = sentence.split( )
l1 = []
for x in l:
    if l.count(x) > 1:
        continue
    else:
        l1.append(x)
print("Sentence after removing duplicate words:", ' '.join(l1))

# b
sentence = input("Enter a sentence:")
l2 = sentence.split()
from collections import Counter
a = Counter(l2)
b = ' '.join(a.keys())
print(b)