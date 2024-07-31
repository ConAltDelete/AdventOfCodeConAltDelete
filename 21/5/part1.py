import math

file = open("lines","r")

coords = {}

for line in file:
    c1, c2 = line.split(" -> ")
    c1 = tuple(int(i) for i in c1.split(","))
    c2 = tuple(int(i) for i in c2.split(","))
    
    diff = (c2[0]-c1[0],c2[1]-c1[1])

    sign = lambda a: (a>0) - (a<0)
    
    norm = (sign(diff[0]) * int(diff[0] != 0), sign(diff[1]) * int(diff[1] != 0))
    
    print(norm) 
    
    current_point = c1

    print(current_point,c2,diff)
    
    while current_point != c2:
        if current_point in coords:
            coords[current_point] += 1
        else:
            coords[current_point] = 1

        current_point = (current_point[0] + norm[0], current_point[1] + norm[1])
    
    if current_point in coords:
        coords[current_point] += 1
    else:
        coords[current_point] = 1

print(len([i for i in coords if coords[i] > 1]))

