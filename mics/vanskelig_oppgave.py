
import logging
logging.basicConfig(filename="./mics/vo.log", encoding='utf-8', filemode="w", level=logging.DEBUG)
from typing import Callable, Generator, Any
from sympy import isprime
import aux_functions as aux

maximum_value = 30
forventet_resultat = 52

tell = 0

radius = dict()

def N_valid(parameter_space: Callable[[Any],Generator[Any,None,None]], filter: Callable[[Any],bool], **kargs) -> int:
    # checks how many elements in parameter_space passes the filter
    return sum(1 for i in parameter_space(**kargs) if filter(i))

def Generate_parameter_space(parameter_function: Callable[[Any],Generator[Any,None,None]], transformer_function: Callable[[Any],Any],**kargs) -> Generator[Any,None,None]:
    for params in parameter_function(**kargs):
        for potential_solution in transformer_function(*params):
            yield potential_solution

def Pyhtagorean_validator(test_case: tuple[int,...]) -> bool:
    if sum(k**2 for k in test_case[:-1]) != test_case[-1]**2:
        logging.info("FAILED: {}, not a valid pythagorean triple".format(test_case))
        return False
    if any(l > n for l,n in zip(test_case,test_case[1:])):
        logging.info("FAILED: {}, not in ascending order".format(test_case))
        return False
    if any(i <= 0 for i in test_case):
        logging.info("FAILED: {}, negative or zero value".format(test_case))
        return False
    if any(i > maximum_value for i in test_case):
        logging.info("FAILED: {}, value too large".format(test_case))
        return False
    logging.info("PASSED: {}".format(test_case))
    return True

def parameter_filter(*N:int) -> bool:
            # Gitt en tuple med vardier, skjekk om de er gyldige
            
            ab = N[0]**2 + N[1]**2

            if (N[0] % 2) != (N[1] % 2): # differen pairity
                k = N[0] // 2
                j = N[1] // 2
                pass

            if isprime(ab): # if ab is a prime number
                if (((ab-1)/2 > maximum_value) \
                | ((ab+1)/2 > maximum_value)):
                     return False
                
            if (ab % 2) == 0: # ab even case
                 pass
            
            if (ab %2) != 0: # ab odd case
                 pass
            

            return True

def two_ints():
    multiplum_value = 4 # I don't know why this works but comes from c(d-1)^2 - d <= 0
    upper_bound_a = int(multiplum_value + (maximum_value*multiplum_value)**0.5)
    upper_bound_b = lambda m,a: int(((m**2 - a**2) / 2)**0.5)+1 # pushes down the upper bound if a is large
    for a in range(1,upper_bound_a):
        for b in range(a,upper_bound_b(maximum_value,a)):
            if parameter_filter(a,b):
                yield (a,b)

number_of_valids = N_valid(
    parameter_space=Generate_parameter_space,
    filter=Pyhtagorean_validator,
    parameter_function=two_ints,
    transformer_function=aux.quad_py_2
    )

prosent_of_calls = number_of_valids / aux.calls["quad_py_2"]

print("antall gyldige: {}/{}, som git prosent {}".format(number_of_valids,forventet_resultat,prosent_of_calls))
