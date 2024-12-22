from collections import defaultdict
import logging
from typing import Generator, Callable
from math import log as ln

calls = defaultdict(int)

def call_counter(func: Callable):
    def wrapper(*args, **kwargs):
        # global calls
        calls[func.__name__] += 1
        return func(*args, **kwargs)
    return wrapper

def quad_py(m:int,n:int,k:int) -> tuple[int,int,int]:
    return (
        m**2 - n**2 - k**2,
        2*m*n,
        2*m*k,
        m**2 + n**2 + k**2
        )

def factor(n: int):
    for i in range(1, int(n ** 0.5) ):
        if (n % i == 0):
            yield i

@call_counter
def quad_py_2(a: int,b: int) -> Generator[tuple[int,int,int,int],None,None]:
    for fac in factor(lm_test := a**2 + b**2):
        if fac > -b + (a**2 + 2*b**2)**0.5:
            continue
        if ((lm_test - fac**2) % 2) != 0:
            continue
        test_yield = (
            a,
            b,
            (lm_test - fac**2) // (2*fac),
            (lm_test + fac**2) // (2*fac)
        )
        if test_yield[2] < 0 or test_yield[3] < 0:
            logging.info("negative value in {}".format(test_yield))
            continue
        yield test_yield