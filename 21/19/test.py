import numpy as np

base_coord = [(1,0,0),(0,1,0),(0,0,1)]

all_rot = set(base_coord)

while True:
    found = set()
    
    for e_1 in all_rot:
        for e_2 in [k for k in all_rot if k != e_1]:
            a = tuple(np.cross(e_1,e_2))
            b = tuple(np.cross(e_2,e_1))

            if a not in all_rot:
                found.add(a)
            if b not in all_rot:
                found.add(b)

    if len(found) == 0:
        break

    all_rot |= found
    

print(all_rot,len(all_rot))
