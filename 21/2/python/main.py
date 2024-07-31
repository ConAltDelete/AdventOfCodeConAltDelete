import sys

path = sys.argv[1]

direc = {
        "forward": lambda x: [x,x,0],
        "down": lambda x: [0,0,x],
        "up": lambda x: [0,0,-x]
        }

data = {
        "horiz" : 0,
        "depth" : 0,
        "aim"   : 0
        }

for command in open(path,"r"):
    command = command.split(" ")
    change = direc[command[0]](int(command[1]))
    data["horiz"] += change[0]
    data["aim"]   += change[2]
    data["depth"] += change[1] * data["aim"]

print(data,data["horiz"]*data["depth"])
