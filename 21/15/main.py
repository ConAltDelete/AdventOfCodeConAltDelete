def solve(p,G,max_x,max_y,DP):
    if p in DP:
        return DP[p]
    if not(0<=p[0]<max_x) or not(0<=p[1]<max_y):
        return float("inf")
    if p == (max_x -1,max_y-1):
        return G[p]
    ans = G[p] + min(solve((p[0]+1,p[1]),G,max_x,max_y,DP),solve((p[0],p[1]+1),G,max_x,max_y,DP))
    DP[p] = ans
    return ans

def surround(p):
    m = [
            (0,1),(0,-1),(1,0),(-1,0)
        ]
    return filter(lambda x: ( 500 > x[0] >= 0) and (500 > x[1] >= 0),map(lambda x: (p[0] + x[0], p[1] + x[1]),m))


def const_path(cameFrom, current,G):
    total = 0
    now = current
    #breakpoint()
    while now != (0,0):
        total += G[now]
        now = cameFrom[now]
    return total

def A_star(p0,p1,G,h):
    openSet = set([p0])

    cameFrom = dict()

    gScore = {p:float("inf") for p in G}
    gScore[p0] = 0

    fScore = {p:float("inf") for p in G}
    fScore[p0] = h(p0,p1,G)

    while len(openSet) != 0:
        current = min(openSet, key= lambda x: fScore[x])

        if current == p1:
            return const_path(cameFrom,current,G)

        openSet.discard(current)

        for p in surround(current):
            tentive_gScore = gScore[current] + G[p]
            if tentive_gScore < gScore[p]:
                cameFrom[p] = current
                gScore[p] = tentive_gScore
                fScore[p] = tentive_gScore + h(p,p1,G)
                if p not in openSet:
                    openSet.add(p)

    return None



def part1():
    file = open("input","r")
    
    G = dict()

    i = 0
    j = 0

    for line in file:
        for num in enumerate(line[:-1]):
            G[(num[0],i)] = int(num[1])
            if num[0] > j:
                j = num[0]

        i += 1


    DP = {}

    print(solve((0,0),G,j+1,i, DP=DP) - G[(0,0)])

def h(p1,p2,G:dict):

    total = abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])
    
    #diff = (p2[0] - p1[0], p2[1] - p1[1])

    #norm = (0,0)
    
    #if abs(diff[0]) > abs(diff[1]):
    #    norm = (1,0)
    #else:
    #    norm = (0, 1)
    
    #now = p1

    #total = 0

    #while now != p2:
    #    now = (now[0] + norm[0], now[1] + norm[1])
    #    diff = (p2[0] - now[0], p2[1] - now[1])
    #    if abs(diff[0]) > abs(diff[1]):
    #        norm = (1,0)
    #    else:
    #        norm = (0,1)
    #    total += G[now]
    #total += G[p2]

    return total

def part2():
    file = open("input","r")

    G = dict()

    i = 0
    j = 0

    for line in file:
        for num in enumerate(line[:-1]):
            G[(num[0],i)] = int(num[1])

        i += 1

    j = max(G.keys(), key= lambda x: x[1])[1]

    new_G = G.copy()

    for k in range(5):
        for z in range(5):
            if k == 0 and z == 0:
                continue
            for p in G.keys():
                new_p = (p[0] + k*i, p[1] + z*(j+1))
                val = G[p] + k + z
                if val > 9:
                    val -= 9
                new_G[new_p] = val

    print(A_star((0,0),(499,499),new_G, h))

if __name__ == "__main__":
	print("part 1: ",end="")
	part1()
	print("part 2: ",end="")
	part2()

