import sys

path = sys.argv[1]

data = []

for line in open(path,"r"):
    data.append(line[:-1])

oxygen_T = [[int(data[y][x]) for y in range(len(data)) ] for x in range(len(data[0]))]
co2_T = [[int(data[y][x]) for y in range(len(data)) ] for x in range(len(data[0]))]

oxygen = list(data)
co2 = list(data)

value_bit = 0

while len(oxygen)*len(co2) > 1:
    if len(oxygen) > 1:
        # oxygen
        oxy_common = int(len(oxygen_T[value_bit])-sum(oxygen_T[value_bit]) <= len(oxygen_T[value_bit])/2)
        temp_oxy = []
        for row in oxygen:
            if int(row[value_bit]) == oxy_common:
                temp_oxy.append(row)
        oxygen = list(temp_oxy)
        
        oxygen_T = [[int(oxygen[y][x]) for y in range(len(oxygen)) ] for x in range(len(oxygen[0]))]
    if len(co2) > 1:
        # co2
        co2_common = int(len(co2_T[value_bit])-sum(co2_T[value_bit]) > len(co2_T[value_bit])/2)
        temp_co2 = []
        for row in co2:
            if int(row[value_bit]) == co2_common:
                temp_co2.append(row)
        
        co2 = list(temp_co2)

        co2_T = [[int(co2[y][x]) for y in range(len(co2)) ] for x in range(len(co2[0]))]

    value_bit += 1

print(oxygen,co2,int(oxygen[0],2)*int(co2[0],2))
