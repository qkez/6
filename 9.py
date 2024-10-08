listt=[]
s=0
from random import randint
for i in range (10):
    listt.append(randint(1,10))
for k in range(1):
    print(listt)
for j in listt:
    s+=j
for m in range(1):
    print(s)
