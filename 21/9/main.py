def test():
    file = open("test","r")

    heatmap = dict()
    

    index_row = 0
    for row in file.readlines():
        row = row[:-1]
        print(row)
        for col in enumerate(list(row)):
            heatmap[(index_row,col[0])] = int(col[1])
        index_row += 1

    minimum = set()

    total = 0

    for p,v in heatmap.items():
        adi = gen_next(p,0,9,0,4)
        print(p,adi)
        if p == mini(adi,dik = heatmap):
            minimum.add(p)
    print(minimum)
    for p in minimum:
        total += heatmap[p] + 1

    print(total)

def mini(a, dik = None):
    small = 10
    small_key = ()
    for key in a:
        v = a[key] if dik == None else dik[key]
        if v < small:
            small = v
            small_key = key
    #print(small_key)
    return small_key

def gen_next(p,x0,x1,y0,y1):
    M = [
            (1,0),
            (0,-1),(0,0),(0,1),
            (-1,0)
        ]
    ret = []
    for m in M:
        new_p = (p[0] + m[0],p[1]+m[1])
        if all([y0 <= new_p[0] <= y1, x0 <= new_p[1] <= x1]):
            ret.append(new_p)

    return ret

def get_size(p,dikt):

    stack = set()

    seen = set()

    bz = set()

    stack.add(p)
    bz.add(p)

    while len(stack) != 0:
        q = stack.pop()
        if dikt[q] != 9 and (q not in seen):
            seen.add(q)
            bz.add(q)
            N = gen_next(q,0,99,0,99)
            for n in [a for a in N if a != q]:
                stack.add(n)

    return len(bz)





def part2():
    file = open("heat","r")

    heatmap = dict()
    

    index_row = 0
    for row in file.readlines():
        row = row[:-1]
        for col in enumerate(list(row)):
            heatmap[(index_row,col[0])] = int(col[1])
        index_row += 1
    
    file.close()

    minimum = set()

    adi = set()

    # First pass

    for key,value in heatmap.items():
        if value == 9:
            adi.add(key)
    
    # second pass

    while len(adi) != 0:
        remove_key = set()
        adi_next = set()
        for p in adi:
            adi_n = gen_next(p,0,99,0,99)

            if p == min(adi_n,key = lambda x: heatmap[x]):
                minimum.add(p)
            else:
                for q in [a for a in adi_n if a != p]:
                    if heatmap[q] < heatmap[p]:
                        adi_next.add(q)
            remove_key.add(p)
        
        adi = (adi | adi_next) - remove_key

    # flow

    sizes = list()

    for point in minimum:
        sizes.append(get_size(point, heatmap))

    tre_big = []

    for _ in range(3):
        big = max(sizes)
        tre_big.append(big)
        sizes.remove(big)

    total = 1
    for a in tre_big:
        total *= a

    print(total)


def part1():
    file = open("heat","r")

    heatmap = dict()
    

    index_row = 0
    for row in file.readlines():
        row = row[:-1]
        for col in enumerate(list(row)):
            heatmap[(index_row,col[0])] = int(col[1])
        index_row += 1
    
    file.close()

    minimum = set()

    adi = set()

    # First pass

    for key,value in heatmap.items():
        if value == 9:
            adi.add(key)
    
    # second pass

    while len(adi) != 0:
        remove_key = set()
        adi_next = set()
        for p in adi:
            adi_n = gen_next(p,0,99,0,99)

            if p == min(adi_n,key = lambda x: heatmap[x]):
                minimum.add(p)
            else:
                for q in [a for a in adi_n if a != p]:
                    if heatmap[q] < heatmap[p]:
                        adi_next.add(q)
            remove_key.add(p)
        
        adi = (adi | adi_next) - remove_key

    total = 0
    
    for p in minimum:
        total += heatmap[p] + 1

    print(total)

if __name__ == "__main__":
    print("part 1: ",end="")
    part1()
    print("part 2: ",end="")
    part2()
