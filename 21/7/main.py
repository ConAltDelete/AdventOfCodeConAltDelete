
def part1():
    file = open("crab","r")

    array = [int(a) for a in file.read().split(",")]

    file.close()

    array = sorted(array)

    mid = array[int(len(array)/2)-1]

    total = 0

    for n in array:
        total += abs(n-mid)

    print(total)

def part2():
    file = open("crab","r")

    array = sorted([int(a) for a in file.read().split(",")])

    file.close()

    collected_sum = sum(array)//len(array)

    total = 0

    for n in array:
        total += (n-collected_sum)**2 + abs(n-collected_sum)

    print(total/2)

if __name__ == "__main__":
    print("part 1:",end = " ")
    part1()

    print("part 2:", end = " ")
    part2()
