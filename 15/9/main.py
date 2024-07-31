def calc_path(p,path,length):
    tot = 0

    travel = [p]
    
    while len(travel) != length:
        current_p = travel[-1]
        #breakpoint()
        rem_path = list(filter(lambda x: current_p in x and any(a not in travel for a in x), path))

        next_p = min(rem_path, key= lambda x: path[x])
        
        tot += path[next_p]

        travel.append([a for a in next_p if a != current_p][0])

    return tot

def calc_path_max(p,path,length):
    tot = 0

    travel = [p]
    
    while len(travel) != length:
        current_p = travel[-1]
        #breakpoint()
        rem_path = list(filter(lambda x: current_p in x and any(a not in travel for a in x), path))

        next_p = max(rem_path, key= lambda x: path[x])
        
        tot += path[next_p]

        travel.append([a for a in next_p if a != current_p][0])

    return tot

def part2():
    file = open("input","r")

    paths = dict()

    points = set()

    for line in file:
        p1, arg = line[:-1].split(" to ")
        p2, length = arg.split(" = ")

        paths[(p1,p2)] = int(length)

        points.add(p1)
        points.add(p2)

    lengths = []

    for p in points:
        lengths.append(calc_path_max(p,paths,len(points)))

    print(max(lengths))

def part1():
    file = open("input","r")

    paths = dict()

    points = set()

    for line in file:
        p1, arg = line[:-1].split(" to ")
        p2, length = arg.split(" = ")

        paths[(p1,p2)] = int(length)

        points.add(p1)
        points.add(p2)

    lengths = []

    for p in points:
        lengths.append(calc_path(p,paths,len(points)))

    print(min(lengths))
    


part1()
part2()
