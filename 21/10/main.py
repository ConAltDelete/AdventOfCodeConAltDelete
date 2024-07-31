def part1():
    file = open("input","r")
    score = {
            ")":3,
            "]":57,
            "}":1197,
            ">":25137
            }
    total = 0

    for line in file:
        stack = []

        opening = "{[(<"
        closing = "}])>"
        pair = {"[]","<>","{}","()"}

        line = line[:-1]
        for char in line:
            if char in opening:
                stack.append(char)
            if char in closing:
                left = stack.pop()
                test = left + char
                if test not in pair:
                    total += score[char]
                    break

            

    print(total)


def part2():
    file = open("input","r")

    points = {
            ")":1,
            "]":2,
            "}":3,
            ">":4
        }

    inverse = {
        "(":")",
        "[":"]",
        "{":"}",
        "<":">"
    }

    opening = "{[(<"
    closing = "}])>"
    pair = {"[]","<>","{}","()"}
    
    scores = []

    for line in file:
        score = 0
        stack = []
        broken = False


        line = line[:-1]
        for char in line:
            if char in opening:
                stack.append(char)
            if char in closing:
                left = stack.pop()
                if left+char not in pair:
                    broken = True
                    break
        
        if broken:
            continue

        if len(stack) != 0:
            for bracket in stack[::-1]:
                score *= 5
                score += points[inverse[bracket]]

        scores.append(score)

    mid = len(scores)//2

    scores = sorted(scores)

    print(scores[mid])

if __name__ == "__main__":
	print("part 1: ",end="")
	part1()
	print("part 2: ",end="")
	part2()

