import sys

path = sys.argv[1]

total = 0

gamma = []

data = []

for line in open(path,"r"):
    line = line[:-1]
    total += 1
    if len(data) == 0:
        data = [0 for _ in range(len(line))]
        gamma = [0 for _ in range(len(line))]

    for bit in range(len(line)):
        if line[bit] == "1":
            data[bit] += 1
        gamma[bit] = str(int(total - data[bit] < total/2))

epsilon = [str(int(not(int(p)))) for p in gamma]

int_gamma = int("".join(gamma),2)
int_epsilon = int("".join(epsilon),2)


print("Gamma:",int_gamma,"\nepsilon:",int_epsilon,"\npower:", int_gamma*int_epsilon)
