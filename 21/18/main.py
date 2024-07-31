import numpy as np


class snailNum:
    def __init__(self,num: list, depth = 0) -> None:
        if type(num) is snailNum:
            self.left = num.left
            self.right = num.right
            self.depth = num.depth
        else:
            self.left: int | snailNum = num[0]
            self.right: int | snailNum = num[-1]
            self.depth: int = depth


        if type(self.left) is list:
            self.left = snailNum(self.left,depth = self.depth + 1)
        if type(self.right) is list:
            self.right = snailNum(self.right,depth = self.depth + 1)

    def __add__(self,other):
        new = snailNum([self,other])
        new.update_()
        return new

    def update_depth(self, n = -1):
        if self.depth <= n or self.depth > n+1:
            self.depth = n + 1

        if type(self.left) is snailNum:
            self.left.update_depth(self.depth)
        if type(self.right) is snailNum:
            self.right.update_depth(self.depth)
    
    def magnitude(self) -> int:
        mag = 0

        if type(self.left) is int:
            mag += 3*self.left
        elif type(self.left) is snailNum:
            mag += 3*self.left.magnitude()

        if type(self.right) is int:
            mag += 2*self.right
        elif type(self.right) is snailNum:
            mag += 2*self.right.magnitude()

        return mag

    def __eq__(self, other):
        
        total = True

        if type(self.left) is int and type(other.left) is int:
            total = (self.left == other.left) and (self.depth == other.depth)
        elif type(self.left) is snailNum and type(other.left) is snailNum:
            total = (self.left == other.left) and (self.depth == other.depth)
        else:
            total = False
        
        if total == False:
            return False

        if type(self.right) is int and type(other.right) is int:
            total = (self.right == other.right) and (self.depth == other.depth)
        elif type(self.right) is snailNum and type(other.right) is snailNum:
            total = (self.right == other.right) and (self.depth == other.depth)
        else:
            total = False

        return total

    def update_(self) -> None:
        self.update_depth()

        something = True

        while something:
            if self.explode():
                continue
            if self.split():
                continue

            something = False
    
    def feed(self,n: int,left: bool) -> None:
        if type(self.left) is int and left:
            self.left += n
        elif type(self.right) is int and not(left):
            self.right += n
        elif type(self.left) is snailNum and left:
            self.left.feed(n,left)
        elif type(self.right) is snailNum and not(left):
            self.right.feed(n,left)


    def explode(self) -> bool | tuple[int,int,bool]:
        ret = False

        if type(self.left) is int and type(self.right) is int and self.depth > 3:
            return (self.left, self.right, True)
        elif type(self.left) is int and type(self.right) is int and self.depth < 4:
            return False

        if type(self.left) is snailNum:
            check = self.left.explode()
            if check == True:
                return True
            elif type(check) is tuple:
                if check[2]:
                    self.left = 0

                check_list = list(check)

                if check_list[1] != 0 and type(self.right) is int:
                    self.right += check_list[1]
                elif check_list[1] != 0 and type(self.right) is snailNum:
                    self.right.feed(check_list[1],left=True)

                if self.depth == 0:
                    return True
                else:
                    return (check_list[0],0,False)


        if type(self.right) is snailNum:
            check = self.right.explode()
            if check == True:
                return True
            elif type(check) is tuple:
                if check[2]:
                    self.right = 0

                check_list = list(check)

                if check_list[0] != 0 and type(self.left) is int:
                    self.left += check_list[0]
                elif check_list[0] != 0 and type(self.left) is snailNum:
                    self.left.feed(check_list[0],left=False)

                if self.depth == 0:
                    return True
                else:
                    return (0,check_list[1],False)

        return ret


    def split(self) -> bool:

        if type(self.left) is int:
            if self.left > 9:
                self.left = snailNum( [int( self.left / 2 ),int(np.ceil( self.left / 2 ))] , depth= self.depth + 1)
                return True
        elif type(self.left) is snailNum:
            check = self.left.split()
            if check:
                return True
        if type(self.right) is int:
            if self.right > 9:
                self.right = snailNum( [int( self.right / 2 ),int(np.ceil( self.right / 2 ))] , depth= self.depth + 1)
                return True
        elif type(self.right) is snailNum:
            check = self.right.split()
            if check:
                return True

        return False

    def __repr__(self) -> str:
        ret = "["
        if type(self.left) is int:
            ret += str(self.left)
        else:
            ret += repr(self.left)

        ret += ","
        if type(self.right) is int:
            ret += str(self.right)
        else:
            ret += repr(self.right)
        
        ret += "]"

        return ret



def part1():
    file = open("input","r")
    
    numbers = list()

    for line in file:
        line = eval(line[:-1])

        numbers.append(snailNum(line))
    
    total = numbers[0]
    
    for n in numbers[1:]:
        total += n
    
    print(total.magnitude())


def part2():
    file = open("input","r")

    number = list()

    for line in file:
        line = eval(line[:-1])

        number.append(line)
    
    #total = numbers[0]
    
    #for n in numbers[1:]:
    #    total += n
    
    #print(total, total.magnitude())

    total = list()

    for a in range(len(number)):
        for b in [k for k in range(len(number)) if k != a]:
            s = snailNum(number[a]) + snailNum(number[b])
            total.append(s.magnitude())
    
    print(max(total))

if __name__ == "__main__":
	print("part 1: ",end="")
	part1()
	print("part 2: ",end="")
	part2()

