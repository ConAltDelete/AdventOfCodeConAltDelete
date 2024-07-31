
def forbidden(s):
    for f in ["ab","cd","pq","xy"]:
        if s.count(f) > 0:
            return True
    return False

def doubble(s):
    for l in "abcdefghijklmnopqrstuvwxyz":
        if s.count(l+l) > 0:
            return True
    return False

def dubdub(s):
    for i in range(len(s)-1):
        pair = s[i:i+2]
        if s.count(pair)>1:
            return True
    return False

def rep_two(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False

def aeiou(s):
    c = [int(s.count(a)) for a in ["a","e","i","o","u"]]
    if sum(c) > 2:
        return True
    return False

def part2():
    file = open("input","r")

    nice = 0

    for line in file:
        line = line[:-1]
        if dubdub(line) and rep_two(line):
            nice += 1

    print(nice)


def part1():
    file = open("input","r")

    nice = 0

    for line in file:
        line = line[:-1]

        if forbidden(line):
            continue

        if not(doubble(line)):
            continue

        if not(aeiou(line)):
            continue

        nice += 1

    print(nice)

part1()
part2()

