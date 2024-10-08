listt=[]
from random import randint
for i in range (10):
    listt.append(randint(1,10))
for k in range(1):
    print(listt)
listt.sort()
print(listt[0])