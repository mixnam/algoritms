#-*- coding:utf-8 -*-
import random

def insert_sort(a):
    for i in range(1,len(a)+1):
        j = i - 1
        while j > 0 and a[j] < a[j-1]:
            a[j],a[j-1] = a[j-1],a[j]
            j -= 1

a = list(range(10000))
a.extend([5,5])
random.shuffle(a)

print(a)
insert_sort(a)
print(a)