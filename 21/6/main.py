
def part1():
    file = open("state","r")
    state = [int(a) for a in file.read().split(",")]

    for _ in range(80):
        intermedian = 0
        for i in range(len(state)):
            state[i] -= 1
            if state[i] < 0:
                state[i] = 6
                intermedian += 1
        for i in range(intermedian):
            state.append(8)

    print(len(state))

def part2():
    file = open("state","r")
    state = [int(a) for a in file.read().split(",")]

    collection = dict()

    for fish in state:
        if fish not in collection:
            collection[fish] = 0
        collection[fish] += 1

    for day in range(256):
        y = {n:0 for n in range(9)}
        for x,count in collection.items():
            if x == 0:
                y[6] += count
                y[8] += count
            else:
                y[x-1] += count

        collection = y

    print(sum(collection.values()))

if __name__ == "__main__":
    part2()
