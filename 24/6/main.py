
class Guard:
    def __init__(self,start_pos:complex):
        self.compl_pos: complex = start_pos # fourth quadrent
        self.mov_vector: complex = 0+1j
        self.visit_pos = set([(self.compl_pos,self.mov_vector)])
        self.board_limits = 0+0j
        self.looped = False
        self.loop_set = set()
        self.boardbreak_set = set()

    def move(self,board: set[complex]) -> bool:
        self.compl_pos += self.mov_vector
        if self.compl_pos in board:
            self.compl_pos -= self.mov_vector
            self.mov_vector *= -1j
            return True
        elif (abs(self.compl_pos.real) >= abs(board_limits.real)) | (abs(self.compl_pos.imag) >= abs(board_limits.imag)):
            return False
        elif ((self.compl_pos,self.mov_vector) in self.visit_pos): # loop found
            self.looped = True
            return False
        self.visit_pos.add((self.compl_pos,self.mov_vector))
        return True

def draw_map(guard: Guard,maping:set[complex])->list[list[str]]:
    init_map = [
        ["." for _ in range(int(guard.board_limits.real))] for _ in range(int(abs(guard.board_limits.imag)))
    ]

    for point in maping:
        init_map[-int(point.imag)][int(point.real)] = "#"
    for Vpoint,_ in guard.visit_pos:
        init_map[-int(Vpoint.imag)][int(Vpoint.real)] = "X"
    
    return init_map

import re

if __name__ == "__main__":

    board = set()
    pattern_obst = "#"
    pattern_guard = "^"
    guard = None
    steps = 0
    map_width = 0
    map_hight = 0

    loop_set = set()
    boardbreak_set = set()

    with open("./6/input","r") as f:
        for y,line in enumerate(f):
            map_width = len(line)
            board.update([mat.start() + (y*-1j) for mat in re.finditer(string=line,pattern=pattern_obst)])
            if (g_find := line.find("^")) >= 0:
                print("found guard at {},{}".format(g_find,y))
                gard_pos = g_find + (y*-1j)
            map_hight = y+1
    
    board_copy = board.copy()
    board_limits = map_width + (map_hight * -1j)

    guard = Guard(
                start_pos= gard_pos
            )
    guard.board_limits = board_limits
    guard.loop_set = loop_set
    guard.boardbreak_set = boardbreak_set

    while guard.move(board=board):
               pass

    base_path = {g[0] for g in guard.visit_pos.copy()}
    looped = 0

    for p_ in base_path - {gard_pos}:
            guard = Guard(
                start_pos= gard_pos
            )

            guard.board_limits = board_limits
            guard.loop_set = loop_set
            guard.boardbreak_set = boardbreak_set

            board = board_copy.union({p_})
            
            while guard.move(board=board):
               pass

            #for row in draw_map(guard=guard,maping= board):
            #    print("".join(row))
            
            if guard.looped:
                #print("It looped!")
                looped += 1
                #loop_set.update(guard.visit_pos)
            elif not(guard.looped):
                pass
                #print("Did not loop...")
                #boardbreak_set.update(guard.visit_pos)

    
    print(map_hight,map_width)



    print("Part 1: {} unique places".format(len(base_path)))
    print("Part 2: There are {} loop positions.".format(looped))