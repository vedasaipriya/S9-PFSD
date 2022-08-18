'''import calc
print(calc.add())
print(calc.sqrt())'''
'''import sys
print(sys.path)'''

'''
import datetime
a = datetime.datetime.now()
print(a)
print(a.year)'''

'''import math as m
#print(m.sqrt(5))'''

'''import math
a=max(5,10,15)
b=min(5,10,15)
print(a,b)'''

import re as r

a = "i prepared to prepare well for exams "
b = r.findall("prepare", a)
print(b)
print(r.search("amep", a))
print(r.sub("prepare","rep",a))
print(r.split(" ",a))

