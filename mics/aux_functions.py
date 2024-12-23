from collections import defaultdict
import logging
from typing import Generator, Callable
from sympy import divisors, isprime
from math import inf, log as ln
import testing_framework as tf
import latexify as lt
calls = defaultdict(int)


def brute_force(max_val:int)->int:
    total_count = 0
    for a in range(1,max_val):
        for b in range(a,max_val):
            for c in range(b,max_val):
                test_abc = a**2 + b**2 + c**2
                if (test_abc**0.5 != int(test_abc**0.5)):
                    continue
                if (test_abc**0.5 > max_val):
                    continue
                total_count += 1
    return total_count

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
    for i in divisors(n):
        if i**2 < n:
            yield i


def two_ints(maximum_value = inf,parameter_filter = lambda *k: True,factor_filter = lambda *k: True,**kwargs) -> Generator[tuple[int,int,int],None,None]:
    upper_bound_a = int(( maximum_value*3**0.5) /3) # poppes out from c(k-1)^2 - d^2 < 0, subtracts 1 as the range of valid values is smaller.
    upper_bound_b = lambda m,a: int(((m**2 - a**2) / 2)**0.5)+1 # pushes down the upper bound if a is large
    for a in range(1,upper_bound_a):
        for b in range(a,upper_bound_b(maximum_value,a)):
            if not(parameter_filter(a,b,maximum_value = maximum_value,**kwargs)):
                continue
            for fac in factor(a**2 + b**2):
                if not(factor_filter(a,b,fac,maximum_value = maximum_value,**kwargs)):
                    continue
                yield (a,b,fac)


def parameter_filter(*N:int,maximum_value = inf,**kwargs) -> bool:
    # Gitt en tuple med vardier, skjekk om de er gyldige
            
    ab = N[0]**2 + N[1]**2

    if ab > maximum_value**2:
        return False
    discriminant = ab + N[1]**2
    if discriminant > maximum_value**2:
        return False

    if isprime(ab): # if ab is a prime number
                if (((ab-1)/2 > maximum_value) \
                |  ((ab+1)/2 > maximum_value)):
                    return False

    return True


def factor_filter(a,b,fac, maximum_value = inf,**kwarg) -> bool:
    lm_test = a**2 + b**2
    if (lm_test/fac + fac) > 2*maximum_value: # ~70%
        return False
    if (((lm_test/fac) - fac) % 2) != 0: # ~50%
        return False
    if fac > -b + (lm_test + b**2)**0.5: # ~58%
        return False
    return True


@call_counter
def quad_py_2(a: int,b: int, fac: int,**kwarg) -> Generator[tuple[int,int,int,int],None,None]:
        lm_test = a**2 + b**2
        
        test_yield = (
            a,
            b,
            (lm_test - fac**2) // (2*fac),
            (lm_test + fac**2) // (2*fac)
        )
        if test_yield[2] < 0 or test_yield[3] < 0:
            logging.info("negative value in {}".format(test_yield))
            raise ValueError("negative value in {} given values ({},{},{})".format(test_yield,a,b,fac))
        yield test_yield

if __name__ == "__main__":
    maximum_value = 30
    print("Brute force: ", tot:=brute_force(maximum_value))
    print("efficent force: ", tf.N_valid(
    parameter_space=tf.Generate_parameter_space,
    filter=tf.Pyhtagorean_validator,
    parameter_function=two_ints,
    transformer_function=quad_py_2,
    maximum_value = maximum_value,
    parameter_filter = parameter_filter,
    factor_filter = factor_filter
    ))
    print(quad_py_2)
    print("Calls: ", calls)
    print("factor of calls: ", tot/calls["quad_py_2"])
    print("Prosent of calls: ", 100*tot/calls["quad_py_2"])