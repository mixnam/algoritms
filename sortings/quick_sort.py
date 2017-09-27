#-*- coding:utf-8 -*-
import random
import logging

# logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s',
#                     level = logging.DEBUG,
#                     filename = u'mylog.log')

def qsort(a,l,r):
    logging.debug((l,r))
    if r-l <= 1:
        logging.debug("STOP REQURSION")
        return
    else:
        x = random.choice(a[l:r])
        j = l
        count = 0
        logging.debug(x)
        for i in range(l,r):
            if a[i] < x:
                a[i], a[j] = a[j], a[i]
                j += 1
            elif a[i] == x:
                count += 1

        if count == r-l:
            logging.debug("SAME VALUES")
            return

        logging.debug((a[l:j],a[j:r]))
        qsort(a,l,j)
        qsort(a,j,r)

a = list(range(100000))
a.extend([5,5])
random.shuffle(a)

logging.debug(a)
qsort(a,0,len(a))
logging.debug(a)

print(a)