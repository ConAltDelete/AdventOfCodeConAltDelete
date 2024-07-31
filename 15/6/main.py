def command(lights, com):

    direct = {
            "turn": {
                "on": lambda x: x+1,
                "off": lambda x: x-1
                },
            "toggle": lambda x: x+2
        }

    p1 = [int(a) for a in com[0].split(",")]
    p2 = [int(a) for a in com[1].split(",")]

    func = direct[com[2]] if len(com[2:]) == 1 else direct[com[3]][com[2]]
    for i in range(p2[0],p1[0]+1):
        for j in range(p2[1],p1[1]+1):
            lights[(i,j)] = func(lights[(i,j)]) if func(lights[(i,j)]) > 0 else 0
    return lights

def part1():
    file = open("input","r")
    
    lights = {(i,j): 0 for i in range(1000) for j in range(1000)}

    for line in file:
        parse = line[:-1].split(" ")[::-1]
        parse = [parse[0]] + parse[2:]
        
        lights = command(lights, parse)

    print(sum(lights[a] for a in lights))

part1()

