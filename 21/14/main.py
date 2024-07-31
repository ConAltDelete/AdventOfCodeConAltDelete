import numpy as np

def insert_poly(polymer: list[str], poly_dict):
    
    new_polymer = polymer

    i = 0

    while i < len(new_polymer):
        test = tuple(new_polymer[i:i+2])
        if test in poly_dict:
            new_polymer.insert(i+1,poly_dict[test])
            i += 1

        i += 1

    return new_polymer

def insert_poly_dict(polymer: dict[str,int], poly_dict: dict[str,str]) -> dict[str,int]:
    
    new_dict = dict(polymer.copy())
    for key in polymer:
        if key in poly_dict:
            p1, p2 = key[0] + poly_dict[key], poly_dict[key] + key[1]

            occs = polymer[key]

            new_dict[key] -= occs

            new_dict[p1] = new_dict.get(p1,0) + occs
            new_dict[p2] = new_dict.get(p2,0) + occs

    #breakpoint()
    return new_dict

def part1():    
    file = open("test","r")
    polymer = list(file.readline()[:-1])
    file.readline()

    poly_dict = dict()

    for line in file:
        line = line[:-1].split(" -> ")
        poly_dict[tuple(line[0])] = line[1]

    for _ in range(10):
        polymer = insert_poly(polymer, poly_dict)

    counts = np.unique(polymer,return_counts=True)
    polymer_ = dict()
    for i in range(len(polymer)-1):
        polymer_.setdefault("".join(polymer[i:i+2]),0)
        polymer_["".join(polymer[i:i+2])] += 1
    print(max(counts[1]) - min(counts[1]))


def part2():
    file = open("test","r")
    polymer_input = file.readline()[:-1]
    file.readline()

    polymer = dict()

    for i in range(len(polymer_input)-1):
        polymer.setdefault(polymer_input[i:i+2],0)
    
    for key in polymer:
        polymer[key] += 1

    poly_dict = dict()

    for line in file:
        line = line[:-1].split(" -> ")
        poly_dict[line[0]] = line[1]

    for _ in range(40):
        polymer = insert_poly_dict(polymer, poly_dict)

    counts = dict()

    for key in polymer:
        counts[key[0]] = counts.get(key[0],0) + polymer[key]

    counts[polymer_input[-1]] = counts.get(polymer_input[-1],0) + 1

    print(max(counts.values()) - min(counts.values()))

if __name__ == "__main__":
	print("part 1: ",end="")
	part1()
	print("part 2: ",end="")
	part2()

