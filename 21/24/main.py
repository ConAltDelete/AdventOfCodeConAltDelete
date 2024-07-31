model_stack = []

def key_gen():
    n = [int(a) for a in list(str(99999999999999))]
    #list2num = lambda x: sum(list(map(lambda y: y[1]*10**(y[0]),enumerate(x[::-1]))))
    while not(all(a == 1 for a in n)):
        yield list(n)
        n[-1] -= 1
        while any(a <= 0 for a in n):
            finding = n.index(0)
            for i in range(finding,len(n)):
                n[i] = 9
            n[finding-1] -= 1


def key_gen2():
    n = [int(a) for a in list(str(11111111111111))]
    #list2num = lambda x: sum(list(map(lambda y: y[1]*10**(y[0]),enumerate(x[::-1]))))
    while not(all(a == 9 for a in n)):
        yield list(n)
        n[-1] += 1
        while any(a > 9 for a in n):
            finding = n.index(10)
            for i in range(finding,len(n)):
                n[i] = 1
            n[finding-1] += 1

def exe(var, command, *args):
    scaler = 0
    if len(args) > 1:
        if type(args[1]) is str:
            scaler = var[args[1]]
        else:
            scaler = args[1]
    match command:
        case "inp":
            var[args[0]] = model_stack.pop(0)
        case "mul":
            var[args[0]] = var[args[0]] * scaler
        case "add":
            var[args[0]] = var[args[0]] + scaler
        case "div":
            var[args[0]] = int(var[args[0]] / scaler)
        case "mod":
            var[args[0]] = var[args[0]] % scaler
        case "eql":
            var[args[0]] = int(var[args[0]] == scaler)
        case _:
            raise ValueError("unknown command: " + command)
    return var

def part1():
    global model_stack
    file = open("input","r")

    program = []

    for line in file:
        line = line[:-1]

        coms = list(line.split(" "))

        if len(coms) > 2:
            if coms[2][0] == "-" and all( a.isdigit() for a in coms[2][1:]):
                coms[2] = int(coms[2])
            elif all( a.isdigit() for a in coms[2]):
                coms[2] = int(coms[2])
            else:
                pass
        program.append(coms)
    
    known_keys = set()
    list2num = lambda x: sum(list(map(lambda y: y[1]*10**(y[0]),enumerate(x[::-1]))))
    for key in key_gen():
        if list2num(key) in known_keys:
            continue
        model_stack = list(key)
        known_keys.add(list2num(key))
        print("tested:",key)
        variable = {"w":0,"x":0,"y":0,"z":0}
        for ints in program:
            variable = exe(variable,ints[0],*ints[1:])
        if variable["z"] == 0:
            print(list2num(key))
            break
        print("tested:",key[::-1])
        model_stack = list(key[::-1])
        known_keys.add(list2num(key[::-1]))
        variable = {"w":0,"x":0,"y":0,"z":0}
        for ints in program:
            variable = exe(variable,ints[0],*ints[1:])
        if variable["z"] == 0:
            print(list2num(key))
            break
    

def part1_alt():
    global model_stack
    file = open("input","r")

    program = []

    for line in file:
        line = line[:-1]

        coms = list(line.split(" "))

        if len(coms) > 2:
            if coms[2][0] == "-" and all( a.isdigit() for a in coms[2][1:]):
                coms[2] = int(coms[2])
            elif all( a.isdigit() for a in coms[2]):
                coms[2] = int(coms[2])
            else:
                pass
        program.append(coms)
    
    known_keys = set()
    list2num = lambda x: sum(list(map(lambda y: y[1]*10**(y[0]),enumerate(x[::-1]))))
    for key in key_gen2():
        if list2num(key) in known_keys:
            continue
        model_stack = list(key)
        known_keys.add(list2num(key))
        print("tested:",key)
        variable = {"w":0,"x":0,"y":0,"z":0}
        for ints in program:
            variable = exe(variable,ints[0],*ints[1:])
        if variable["z"] == 0:
            print(list2num(key))
            break
        print("tested:",key[::-1])
        model_stack = list(key[::-1])
        known_keys.add(list2num(key[::-1]))
        variable = {"w":0,"x":0,"y":0,"z":0}
        for ints in program:
            variable = exe(variable,ints[0],*ints[1:])
        if variable["z"] == 0:
            print(list2num(key))
            break
        

def part2():
    file = open("input","r")

if __name__ == "__main__":
	print("part 1: ",end="")
	part1_alt()
	print("part 2: ",end="")
	part2()

