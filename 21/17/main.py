import numpy as np

g = np.array((0,-1))

def sim_throw(s,v, limit_point, target):
    point = np.array(s)
    val   = np.array(v)

    y = 0

    while not( abs(point[0]) > abs(limit_point[0]) or point[1] < limit_point[1]):
        
        point += val
        val += d(val) + g

        if point[1] > y:
            y = int(point[1])

        if tuple(point) in target:
            return y,True

    return y,False
    


def d(s):
    if s[0] > 0:
        return np.array((-1,0))
    elif s[0] < 0:
        return np.array((1,0))
    else:
        return np.array((0,0))

def part1():
    file = open("input","r").readline()[13:-1]

    x,y = file.split(", ")
        
    xrange, yrange = [a[2:].split("..") for a in (x,y)]

    c1 = (int(xrange[0]),int(yrange[0]))
    c2 = (int(xrange[1]),int(yrange[1]))

        
    start = (0,0)

    limit_point = [max(c1[0],c2[0], key= lambda x: x**2), min(0, c1[1], c2[1])]

    target = set((a,b) for a in range(min(c1[0],c2[0]),max(c1[0],c2[0]) + 1) for b in range(min(c1[1],c2[1]),max(c1[1],c2[1]) + 1))
    
    x_min = int((2*c1[0])**0.5)
    x_max = c2[0] + 1

    big_y = 0

    for y in range(1, 300):
        for x in range(x_min,x_max + 1):
            sim, ok = sim_throw(s=start, v=(x,y), limit_point = limit_point, target = target)
            if ok and sim > big_y:
                big_y = int(sim)

    print(big_y)

def part2():
    file = open("input","r").readline()[13:-1]

    x,y = file.split(", ")
        
    xrange, yrange = [a[2:].split("..") for a in (x,y)]

    c1 = (int(xrange[0]),int(yrange[0]))
    c2 = (int(xrange[1]),int(yrange[1]))

        
    start = (0,0)

    limit_point = [max(c1[0],c2[0], key= lambda x: x**2), min(0, c1[1], c2[1])]

    target = set((a,b) for a in range(min(c1[0],c2[0]),max(c1[0],c2[0]) + 1) for b in range(min(c1[1],c2[1]),max(c1[1],c2[1]) + 1))
    
    x_min = 1
    x_max = c2[0] + 1

    total = set()

    for y in range(-500, 500):
        for x in range(x_min,x_max + 1):
            sim, ok = sim_throw(s=start, v=(x,y), limit_point = limit_point, target = target)
            if ok:
                total.add((x,y))

    print(len(total))

if __name__ == "__main__":
	print("part 1: ",end="")
	part1()
	print("part 2: ",end="")
	part2()

