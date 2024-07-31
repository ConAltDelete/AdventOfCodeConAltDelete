def dice():
    i = 1
    while True:
        yield i
        i += 1
        if i > 100:
            i = 1

def test():
    k = dice()
    for _ in range(3):
        print(next(k))
    a = dice()
    for _ in range(5):
        print(next(k))
        print(next(a))

permut = [tuple(sorted((a,b,c))) for a in (1,2,3) for b in (1,2,3) for c in (1,2,3)]
permut_coeff = {p:permut.count(p) for p in set(permut)}

game_state = dict()

def dirac_dice(player: int, pos: dict[int,int] ,score: dict[int,int], dice):
    """
    PLAN RECURSION:
        input: insert player, and last score

        - kalkuler permisjoner, kalculer score, og lag en ny grein for hver (om det gir mening)
        - hent antallet fra hvert univers, og summer
        - om spiller vinner denne runden summer antall permisjoner hvor'n vinner og returner antall og spiller i en dict. {player: number of universes}
    """
    if score[player] >= 21:
        if player == 1:
            return {1:permut_coeff[dice],0:0}
        else:
            return {1:0,0:permut_coeff[dice]}
    
    if ( k := (pos[0],pos[1],score[0],score[1]) )in game_state:
        return game_state[k]

    count = {1:0,0:0}

    for p in permut_coeff.keys():
        """
            kalkuler neste move, og legg til poeng.
        """
        other = int(not(player))
        dice_sum = sum(p)
        next_move = dict(pos)
        next_move[other] += dice_sum
        while next_move[other] > 10:
            next_move[other] -= 10
        new_score = dict(score)
        new_score[other] += next_move[other]
        
        temp_wins = dirac_dice(player = other, pos = next_move,score = new_score,dice=p)
        for key in temp_wins:
            count[key] += temp_wins[key]
    
    game_state[(pos[0],pos[1],score[0],score[1])] = count

    return count

def part1():
    file = open("input","r")
    the_dice = dice()

    p1 = 0 
    p2 = 0
    p1_score = 0
    p2_score = 0

    dice_trow = 0
    
    for line in file:
        if line[:8] == "Player 1":
            p1 = int(line[-2:-1])
        else:
            p2 = int(line[-2:-1])

    p1_turn = True

    while p1_score < 1000 and p2_score < 1000:
        
        move = sum(next(the_dice) for _ in range(3))
        
        if p1_turn:
            p1 = (p1 + move)
            while p1 > 10:
                p1 -= 10
            p1_score += p1
        else:
            p2 = (p2 + move)
            while p2 > 10:
                p2 -= 10
            p2_score += p2

        p1_turn ^= True
        
        dice_trow += 3
    
    print(min(p1_score,p2_score)*dice_trow)

def part2():
    file = open("input","r")

    p1 = 0 
    p2 = 0

    scores = {
            0:0,
            1:0
        }

    for line in file:
        if line[:8] == "Player 1":
            p1 = int(line[-2:-1])
        else:
            p2 = int(line[-2:-1])

    scores = dirac_dice(player=0,pos={0:p1,1:p2},score=scores,dice=None)


    print(max(scores.values()))    

def part2_alt():
    p1 = 10-1
    p2 = 2-1
    #p1 = 4-1
    #p2 = 8-1

    # dynamic programming!
    # brute force + memoization.
    # how many possible game states are there?
    # 10 options for p1, 10 options for p2, 21 options for s1, 21 options for s2 -> 10*10*21*21 ~ 40,000
    # total running time ~ state space * non-recursive time for one call ~ 40e3 * 27 ~ 120e4 = ~1M
    p1 = 10-1
    p2 = 2-1
    DP = {} # game state -> answer for that game state
    def count_win(p1, p2, s1, s2):
      # Given that A is at position p1 with score s1, and B is at position p2 with score s2, and A is to move,
      # return (# of universes where player A wins, # of universes where player B wins)
      if s1 >= 21:
        return (1,0)
      if s2 >= 21:
        return (0, 1)
      if (p1, p2, s1, s2) in DP:
        return DP[(p1, p2, s1, s2)]
      ans = (0,0)
      for d1 in [1,2,3]:
        for d2 in [1,2,3]:
          for d3 in [1,2,3]:
            new_p1 = (p1+d1+d2+d3)%10
            new_s1 = s1 + new_p1 + 1

            x1, y1 = count_win(p2, new_p1, s2, new_s1)
            ans = (ans[0]+y1, ans[1]+x1)
      DP[(p1, p2, s1, s2)] = ans
      return ans

    print(max(count_win(p1, p2, 0, 0)))

if __name__ == "__main__":
	print("part 1: ",end="")
	part1()
	print("part 2: ",end="")
	part2()
	#test()
	print("alternativ part 2: ",end="")
	part2_alt()

