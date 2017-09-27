#-*- coding:utf-8 -*-
import random


def divide(a):
    l = len(a)
    if len(a) == 1:
        return a
    else:
        m = (0 + l)//2
        left = divide(a[0:m])
        right = divide(a[m:])
        return merge(left,right)

def merge(a,b):
    c =  []
    i,j = 0,0
    while i < len(a) or j < len(b):
        if i == len(a) or (j < len(b) and a[i] > b[j]):
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    return c

a = list(range(100000))
a.extend([5,5])
random.shuffle(a)

a2 = divide(a)
print(a)
print(a2)
