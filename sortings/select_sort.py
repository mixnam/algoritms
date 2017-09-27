#-*- coding:utf-8 -*-
import random

def select_sort(a):
    for i in range(len(a)):
        c = a[i:]
        index = c.index(min(c))
        print(index)
        if i != index:
            c[index],c[i] = c[i],c[index]

a = list(range(10))
random.shuffle(a)

print(a)
select_sort(a)
print(a)
