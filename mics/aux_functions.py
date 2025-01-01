from collections import defaultdict
import logging
import time
from typing import Generator, Callable
from sympy import divisors, isprime, factorint
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

def permute_count(left_list:list[tuple[int,int]],right_list:list[tuple[int,int]]) -> int:
    """
        Goes trough all possible permutations of the left and right list and checks if they are valid.
        strategy:
            - sort both lists
            - iterate through the left list
            - since both lists are sorted we can iterate through the left list and slowly iterate thought the right list until we find a value equal to or greater than the left value
            - if we reach the end of the right list and we haven't found a higher value -> break the loop
    """
    #count = sum(left <= right for left in left_list for right in right_list)
    count = 0
    left_list.sort()
    right_list.sort()
    r_i = 0
    right = right_list[r_i]
    for left in range(len(left_list)):
        while left_list[left] > right and r_i < len(right_list)-1:
            r_i += 1
            right = right_list[r_i]
        
        if r_i == len(right_list)-1 and left_list[left] > right:
            break
        
        count += len(right_list) - r_i
    return count

def number_match_memeff(maximum) -> int: #! overcounts, must be fixed!
    """
    Computes the number of pythagorean quadruples using distance between squares
    with optimized memory usage
    """
    def generate_left_pairs(m): # mono-increasing function
        upper_bound_a = int(m/(3**0.5))
        for a in range(1, upper_bound_a):
            upper_b = int(((m**2 - a**2) / 2)**0.5) + 1
            for b in range(a, upper_b):
                ab = a**2 + b**2
                if ab % 4 == 2 or ab < 4:
                    continue
                yield ab, b

    def generate_right_pairs(m):
        for c in range(1, m-1):
            for d in range(c+1, m+1):
                cd = d**2 - c**2
                yield cd, c

    count = 0
    # Process in chunks to reduce memory usage
    chunk_size = 50_000_000
    left_chunk = defaultdict(list)
    
    for ab, b in generate_left_pairs(maximum):
        left_chunk[ab].append(b)
        
        if len(left_chunk) >= chunk_size:
            # Process current chunk
            for cd, c in generate_right_pairs(maximum):
                if cd in left_chunk:
                    count += len(left_chunk[cd])
            left_chunk.clear()
    
    # Process remaining pairs
    if left_chunk:
        for cd, c in generate_right_pairs(maximum):
            if cd in left_chunk:
                count += len(left_chunk[cd])
    
    return count

def number_match(maximum) -> int:
    """
        Computes the number of pythagorean quadruples using distance between the two squares
    """
    left_dict = defaultdict(list[int])
    right_dict = defaultdict(list[int])
    upper_bound_a = int(( maximum)/(3**0.5)) # poppes out from c(k-1)^2 - d^2 < 0, subtracts 1 as the range of valid values is smaller.
    upper_bound_b = lambda m,a: int(((m**2 - a**2) / 2)**0.5)+1 # pushes down the upper bound if a is large

    for a in range(1,upper_bound_a):
        for b in range(a,upper_bound_b(maximum,a)):
            if (ab := a**2 + b**2)%4==2 or ab < 4: # ignores 3 as 3 is not a sum of 2 squares; ref: https://oeis.org/A024352
                continue
            left_dict[ab] += [b]

    for c in range(1,maximum-1):
        for d in range(c+1,maximum+1):
            if (cd := d**2 - c**2) not in left_dict:
                continue
            right_dict[cd] += [c]
    
    count = sum(permute_count(left_dict[key],right_dict[key]) for key in right_dict)

    return count

def quad_py(m:int,n:int,k:int) -> tuple[int,int,int]:
    return (
        m**2 - n**2 - k**2,
        2*m*n,
        2*m*k,
        m**2 + n**2 + k**2
        )

def factor(a:int,b:int,maximum_value = inf,**kwargs):
    for i in divisors(n:= a**2 + b**2):
        if i < -maximum_value+(maximum_value**2 + a**2 + b**2)**0.5:
            continue
        if i > int((a**2 + 2*b**2)**0.5 - b):
            logging.debug("FAILED::FACTORING::[a:{}, b:{}, fac:{}] factor is greater than sqrt(a^2+2b^2)-b".format(a,b,i))
            return GeneratorExit
        if i**2 < n:
            yield i


def two_ints(maximum_value = inf,parameter_filter = lambda *k: True,factor_filter = lambda *k: True,**kwargs) -> Generator[tuple[int,int,int],None,None]:
    upper_bound_a = int(( maximum_value*3**0.5) /3) # poppes out from c(k-1)^2 - d^2 < 0, subtracts 1 as the range of valid values is smaller.
    upper_bound_b = lambda m,a: int(((m**2 - a**2) / 2)**0.5)+1 # pushes down the upper bound if a is large
    for a in range(1,upper_bound_a):
        for b in range(a,upper_bound_b(maximum_value,a)):
            if not(parameter_filter(a,b,maximum_value = maximum_value,**kwargs)):
                continue
            for fac in factor(a,b,maximum_value = maximum_value,**kwargs):
                if not(factor_filter(a,b,fac,maximum_value = maximum_value,**kwargs)):
                    #logging.debug("FAILED::FACTOR::[a:{}, b:{}, fac:{}] Could not find suible factors".format(a,b,fac))
                    continue
                yield (a,b,fac)


def parameter_filter(*N:int,maximum_value = inf,**kwargs) -> bool:
    # Gitt en tuple med vardier, skjekk om de er gyldige

    a = N[0]
    b = N[1]
    ab = a**2 + b**2
    
    if (ab%4 == 2 or ab < 4): # ignores 3 as 3 is not a sum of 2 squares; ref: https://oeis.org/A024352
        logging.debug("FAILED::PARAMETER::[a:{}, b:{}] a^2+b^2 is congruent to 2 mod 4".format(N[0],N[1]))
        return False

    if isprime(ab): # if ab is a prime number
                if (((ab-1)/2 > maximum_value) \
                |  ((ab+1)/2 > maximum_value)):
                    logging.debug("FAILED::PARAMETER::[a:{}, b:{}] ab is prime and too large".format(N[0],N[1]))
                    return False
                
    logging.debug("PASSED::PARAMETER::[a:{}, b:{}]".format(a,b))

    return True


def factor_filter(a,b,fac, maximum_value = inf,**kwarg) -> bool:
    lm_test = a**2 + b**2
    
    if fac < -maximum_value+(maximum_value**2 + a**2 +b**2)**0.5: # ~50%
        logging.debug("FAILED::FACTOR::[a:{}, b:{}, fac:{}] factor is smaller than sqrt(d^2+a^2+b^2)-d".format(a,b,fac))
        return False
    if fac > -b + (lm_test + b**2)**0.5: # ~58%
        logging.debug("FAILED::FACTOR::[a:{}, b:{}, fac:{}] factor is greater than sqrt(a^2+2b^2)-b".format(a,b,fac))
        return False

    c_pluss = (lm_test//fac + fac) 
    c_minus = (lm_test//fac - fac)
    if c_pluss > 2*maximum_value or c_minus > 2*maximum_value:
        logging.debug("FAILED::FACTOR::[a:{}, b:{}, fac:{}] c too large".format(a,b,fac))
        return False
    if (c_minus % 2) != 0: # ~50%
        logging.debug("FAILED::FACTOR::[a:{}, b:{}, fac:{}] c not divisible by 2".format(a,b,fac))
        return False

    logging.debug("PASSED::FACTOR::[a:{}, b:{}, fac:{}]".format(a,b,fac))
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
            logging.critical("negative value in {} given values ({},{},{})".format(test_yield,a,b,fac))
            raise ValueError("negative value in {} given values ({},{},{})".format(test_yield,a,b,fac))
        yield test_yield

if __name__ == "__main__":
    import datetime as dt
    maximum_value = 3000
    print("### Testing with maximum value: ", maximum_value, " ###")
    start = time.process_time()
    print("- Number matching:",number_match_memeff(maximum_value))
    end = time.process_time()
    print("\t - Time:",dt.timedelta(seconds=end - start))
    start = time.process_time()
    print("- Number matching:",number_match(maximum_value))
    end = time.process_time()
    print("\t - Time:",dt.timedelta(seconds=end - start))
    start = time.process_time()
    print("- Efficent force: ", tf.N_valid(
    parameter_space=tf.Generate_parameter_space,
    filter=tf.Pyhtagorean_validator,
    parameter_function=two_ints,
    transformer_function=quad_py_2,
    maximum_value = maximum_value,
    parameter_filter = parameter_filter,
    factor_filter = factor_filter
    ))
    end = time.process_time()
    print("\t - Time:",dt.timedelta(seconds=end - start))
    start = time.process_time()
    print("- Brute force: ", tot:=brute_force(maximum_value))
    end = time.process_time()
    print("\t - Time:",dt.timedelta(seconds=end - start))
    print("~ factor of calls: ", tot/calls["quad_py_2"])
    print("~ Prosent of calls: ", 100*tot/calls["quad_py_2"])
    print("Test completed.")
