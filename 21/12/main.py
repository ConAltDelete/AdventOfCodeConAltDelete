def part1():
    file = open("input","r")

    graph = dict() # from : to

    for line in file:
        start, end = (line[:-1]).split("-")
        
        #breakpoint()

        if start in graph:
            graph[start].append(end)
        if end in graph:
            graph[end].append(start)
        
        if start not in graph:
            graph[start] = [end]

        if end not in graph:
            graph[end]   = [start]

    file.close()

    start = ("start",set(["start"]))

    stack = []

    total = 0

    stack.append(start)

    while len(stack) != 0:
        v,small = stack.pop()
        if v == "end":
            total += 1
            continue

        for nodes in graph[v]:
            if nodes not in small:
                new_small = set(small)
                if nodes.islower():
                    new_small.add(nodes)
                stack.append( (nodes,new_small) )


    print(total)





def part2():
    from collections import deque

    file = open("input","r")

    graph = dict() # from : to

    for line in file:
        start, end = line.strip().split("-")
        
        #breakpoint()

        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]

        if end in graph:
            graph[end].append(start)
        else:
            graph[end]   = [start]

    file.close()

    start = ("start",set(["start"]),None)

    total = 0

    stack = deque([start])
    
    breakpoint()

    while stack:
        v,small, tw = stack.popleft()
        if v == "end":
            total += 1
            continue

        for nodes in graph[v]:
            if nodes not in small:
                new_small = set(small)
                if nodes.islower():
                    new_small.add(nodes)
                stack.append( (nodes,new_small,tw) )
            elif (nodes in small) and (tw is None) and (nodes not in ["start","end"]):
                stack.append((nodes,small,nodes))


    print(total)

if __name__ == "__main__":
	print("part 1: ",end="")
	part1()
	print("part 2: ",end="")
	part2()

