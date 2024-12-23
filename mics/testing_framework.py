
from math import inf
import logging
from typing import Any, Callable, Generator


def N_valid(parameter_space: Callable[[Any],Generator[Any,None,None]], filter: Callable[[Any],bool], **kargs) -> int:
    # checks how many elements in parameter_space passes the filter
    total = 0
    try:
        for i in parameter_space(**kargs):
            if filter(i,**kargs):
                total += 1
    except KeyboardInterrupt:
        logging.info("Interrupted")
    return total
    #return sum(1 for i in parameter_space(**kargs) if filter(i))

def Generate_parameter_space(parameter_function: Callable[[Any],Generator[Any,None,None]], transformer_function: Callable[[Any],Any],**kargs) -> Generator[Any,None,None]:
    for params in parameter_function(**kargs):
        for potential_solution in transformer_function(*params,**kargs):
            yield potential_solution

def Pyhtagorean_validator(test_case: tuple[int,...],maximum_value = inf,**kwarg) -> bool:
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