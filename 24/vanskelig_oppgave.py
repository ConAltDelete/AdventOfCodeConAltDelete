
import logging
from typing import Generator


d = 30

tell = 0

radius = dict()

def quad_py(m:int,n:int,k:int) -> tuple[int,int,int]:
    return (
        m**2 - n**2 - k**2,
        2*m*n,
        2*m*k,
        m**2 + n**2 + k**2
        )

def factor(n: int) -> set:
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        if (n % i == 0) & (i**2 < n):
            result.add(i)
    return result

def quad_py_2(a,b) -> Generator[tuple[int,int,int,int],None,None] | int:
    #l = a // 2
    #m = b // 2
    fact_lm = factor(lm_test := a**2 + b**2)
    for fac in fact_lm:
        yield (
            a,
            b,
            (lm_test - fac**2) // (2*fac),
            (lm_test + fac**2) // (2*fac)
        )
    else:
        return 0

set_of_points = set()

logging.basicConfig(filename="vo.log", encoding='utf-8', filemode="w", level=logging.DEBUG)

for m in range(1,d+1):
    for n in range(1,d+1):
            test = quad_py_2(m,n)
            for t in test:
                byte_fail = 0
                # t = sorted(t)
                if t == 0: # fail condition
                    byte_fail |= 0b00001
                if sum(k**2 for k in t[:-1]) != t[-1]**2:
                    byte_fail |= 0b00010
                if any(i < 0 for i in t):
                    byte_fail |= 0b00100
                if t[-1] > d:
                    byte_fail |= 0b01000
                if any(t[i+1] - t[i] < 0 for i in range(len(t)-1)):
                    byte_fail |= 0b10000
                if byte_fail > 0:
                    logging.info("error: {:0<5b}".format(byte_fail))
                    continue
                print(t)
                set_of_points.add(tuple(t))
                tell += 1

print("Antall funn: {}".format(tell))