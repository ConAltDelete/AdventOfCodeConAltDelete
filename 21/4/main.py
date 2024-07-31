import sys

def calc_score(board,remove_nums,num):
    
    comp = set()

    for a in board:
        comp |= a

    unmarked = comp - remove_nums

    return sum(unmarked)*num

def check_if_subset(board, numbers):
    for b in board:
        if b.issubset(numbers):
            return True
    return False

def create_sets(B):
    """
        B = [
            [...],
            [...],
            [...]
        ]
    """
    sets = []

    for row in B:
        sets.append(set(row))
    
    for col in range(len(B[0])):
        sets.append(set([B[row][col] for row in range(len(B)) ]))

    return sets

if __name__ == "__main__":
    file = open("boards","r")

    rand_list = [int(a) for a in file.readline().split(",")]
    
    print(rand_list[:83])

    boards = []

    for line in file:
        if line == "\n":
            boards.append([])
        else:
            row = [int(l) for l in line[:-1].split(" ") if l != ""]
            assert(len(row) == 5)
            boards[-1].append(row)

    sets = []
    for B in boards:
        sets.append(create_sets(B))

    rand_set = set()

    score = 0

    found = False


    for turn,number in enumerate(rand_list):
        rand_set.add(number)
        remove = []
        score_temp = []
        for index,board in enumerate(boards):
            board_set = create_sets(board)
            if check_if_subset(board_set, rand_set):
                score = calc_score(board_set,rand_set, number)
                remove.append(index)

        boards = [a for i,a in enumerate(boards) if i not in remove]

        
        if len(boards) == 0:
            print(board, rand_set,number)
            break


    print(score)
