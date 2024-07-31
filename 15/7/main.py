def commands(com, arg):
    com_dic = {
            "AND": lambda x: x[0] & x[1],
            "OR": lambda x: x[0] | x[1],
            "RSHIFT":lambda x: x[0] >> x[1],
            "LSHIFT":lambda x: x[0] << x[1],
            "NOT": lambda x: ~x[0]
        }

    #breakpoint()

    value = com_dic[com](arg)

    return value

def part1():
    file = open("input","r")
    
    # first pass

    values = dict()

    inst = dict()

    for line in file:
        line = line[:-1]

        do, wire = line.split("->")

        do, wire = do.strip(), wire.strip()

        if do.isnumeric():
            values[wire] = int(do)
        else:
            #breakpoint()
            com = do.split(" ")
            if len(com) == 2:
                inst[wire] = [com[0],com[1]]
            elif len(com) == 1:
                inst[wire] = [com[0]]
            else:
                inst[wire] = [com[1],com[0],com[2]]
    
    #breakpoint()

    values["b"] = 46065

    i = 0

    pre_val = len(inst)

    while len(inst) != 0 and i < len(inst) + 1:
        for test_key in list(inst.keys()):
            args = inst[test_key][1:]
            
            existence = True

            if len(args) == 0:
                if inst[test_key][0] in values:
                    v = values.pop(inst[test_key][0])
                    values[test_key] = v
                continue

            for a in [k for k in args if not(k.isnumeric())]:
                if a not in values:
                    existence = False
            #breakpoint()
            if existence:
                args = [int(a) if a.isnumeric() else values[a] for a in args]
                values[test_key] = commands(inst[test_key][0],args)
        i += 1
    #breakpoint()
    print(values["a"])

part1()

