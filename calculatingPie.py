from math import factorial
from decimal import Decimal as fl
import decimal
decimal.getcontext().prec = 1000 #pie upto 1lac places
def pie(k):
    a = 8**0.5/9801
    blist = []
    for i in range(0,k):
        b1 = factorial(4*i)
        b2 = 1103+26390*i
        b3 = fl(factorial(i))**fl(4)*fl(396)**fl(4*i)
        b = b1*b2/b3
        blist.append(b)
    b = fl(sum(blist))
    ans1 = fl(a)*b
    return 1/ans1

print(pie(100))

