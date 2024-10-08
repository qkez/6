listt=[]
b=0
from random import randint
for i in range(10):
    listt.append(randint(1,10))
for i in range(1):
    print(listt)
for i in listt:
    if listt.count(i)>1:
        listt.remove(i)
print(len(listt))