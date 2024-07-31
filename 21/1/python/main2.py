import sys

data = open(sys.argv[1],"r")

t_sum = []

for point in data:
    t_sum.append(0)

    if len(t_sum) < 3:
        for i in range(len(t_sum)):
            t_sum[i] += int(point)
        continue

    for i in range(1,4):
        t_sum[-i] += int(point)

inc_count = 0

for s in range(1,len(t_sum)):
    if t_sum[s] > t_sum[s-1]:
        inc_count += 1

print(inc_count)
