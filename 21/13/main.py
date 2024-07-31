def fold_paper(paper, axis, coord):
    past_line = set(filter(lambda x: (x[0]>coord) if axis=="x" else (x[1]>coord),paper))
    new_dict = {a:"#" for a in paper if a not in past_line}

    for point in past_line:
        new_x = 2*coord - point[axis == "y"] if axis=="x" else point[0]
        new_y = 2*coord - point[axis == "y"] if axis=="y" else point[1]
        new_dict.update({(new_x,new_y):"#"})

    return new_dict


def part1():
    file = open("input","r")
    paper = dict()
    folding = []

    for line in file:
        line = line[:-1]
        coord = line.split(",")
        if len(coord) == 1 and coord[0] != "":
            folding.append(coord[0])
        elif len(coord) == 2:
            paper[(int(coord[0]),int(coord[1]))] = "#"
    

    axis,coord = folding[0].split("=")
    axis = axis[-1]
    coord = int(coord)

    print(len(fold_paper(paper,axis,coord)))

    



def part2():
    file = open("input","r")
    paper = dict()
    folding = []

    for line in file:
        line = line[:-1]
        coord = line.split(",")
        if len(coord) == 1 and coord[0] != "":
            folding.append(coord[0])
        elif len(coord) == 2:
            paper[(int(coord[0]),int(coord[1]))] = "#"
    

    for fold in folding:
        fold = fold.split("=")
        axis = fold[0][-1]
        coord = int(fold[1])

        paper = fold_paper(paper, axis, coord)

    max_x = max(paper,key = lambda x: x[0])[0]
    max_y = max(paper,key = lambda x: x[1])[1]

    board = [["." for _ in range(max_x + 1)] for _ in range(max_y+1)]

    for p in paper:
        board[p[1]][p[0]] = "#"

    print()

    for line in board:
        print("".join(line))


if __name__ == "__main__":
	print("part 1: ",end="")
	part1()
	print("part 2: ",end="")
	part2()

