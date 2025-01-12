from collections import defaultdict
from dataclasses import dataclass
from typing import List, Tuple
import re

@dataclass
class PythagoreanQuadruple:
    a: int
    b: int
    c: int
    d: int

@dataclass
class FactorFailure:
    a: int
    b: int
    fac: int
    reason: str

@dataclass
class ParameterFailure:
    a: int
    b: int
    reason: str

class LogAnalyzer:
    def __init__(self, logfile: str):
        self.logfile = logfile
        self.factor_failures: List[FactorFailure] = []
        self.param_failures: List[ParameterFailure] = []
        self.validations: List[PythagoreanQuadruple] = []
        
    def parse_log(self):
        factor_pattern = r'FAILED::FACTOR::\[a:(\d+), b:(\d+), fac:(\d+)\] (.+)'
        param_pattern = r'FAILED::PARAMETER::\[a:(\d+), b:(\d+)\] (.+)'
        valid_pattern = r'PASSED::VALIDATION: \((\d+), (\d+), (\d+), (\d+)\)'
        
        with open(self.logfile, 'r') as f:
            for line in f:
                if 'FAILED::FACTOR' in line:
                    match = re.search(factor_pattern, line)
                    if match:
                        self.factor_failures.append(
                            FactorFailure(int(match[1]), int(match[2]), 
                                        int(match[3]), match[4]))
                elif 'FAILED::PARAMETER' in line:
                    match = re.search(param_pattern, line)
                    if match:
                        self.param_failures.append(
                            ParameterFailure(int(match[1]), int(match[2]), 
                                           match[3]))
                elif 'PASSED::VALIDATION' in line:
                    match = re.search(valid_pattern, line)
                    if match:
                        self.validations.append(
                            PythagoreanQuadruple(
                                int(match[1]), int(match[2]),
                                int(match[3]), int(match[4])
                                )
                        )
    
    
    def print_results(self):
        print("## Factor Failures")
        for f in self.factor_failures:
            print(f"- a:{f.a}, b:{f.b}, fac:{f.fac} → {f.reason}")
            
        print("\n## Parameter Failures")
        for p in self.param_failures:
            print(f"- a:{p.a}, b:{p.b} → {p.reason}")

        uniqness = defaultdict(int)
        print("\n## validations")
        for p in self.validations:
            uniqness[(p.a, p.b)] += 1
            print(f"- {p.a}^2 + {p.b}^2 + {p.c}^2 = {p.d}^2")

        print("## Uniqness")
        for S in uniqness:
            print(f"- ({S[0]},{S[1]}) has {uniqness[S]} valid solutions")
        
        print("Max number of valid solutions for a,b: ", max(uniqness.values()))
        print("Min number of valid solutions for a,b: ", min(uniqness.values()))
        
if __name__ == "__main__":
    analyzer = LogAnalyzer("vo.log")
    analyzer.parse_log()
    analyzer.print_results()