import sys

args = sys.argv

assert(len(args) == 2)

file = open(args[1],"r")

pre = None

inc = 0

for data in file:
    if pre == None:
        print(data[:-1], "(N/A - no previous measurement)")
    else:
        print(data[:-1], "(increased)" if int(data) - pre > 0 else "(decreased)")
        inc += int(data) - pre > 0
    pre = float(data)

print(inc)

