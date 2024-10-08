listt=[]
from random import randint
for i in range(20):
    listt.append(randint(1,100))
listt.sort()
listt.reverse()
print(listt)
print(listt[1])