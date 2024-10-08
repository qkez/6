a=0
listt=[]
from random import randint
for i in range(10):
    listt.append(randint(1, 9))
for i in listt:
    a=listt.count(i)
for i in range(1):
    print(listt)
print(a)