
def find_1478(output):

    total = 0

    for digit in output.split(" "):
        

        if len(digit) in [2,3,4,7]:
            total += 1

    return total

def remove_digits(liste, sets):
    new_list = [a for a in liste if set(a) not in sets.values()]
    return new_list

def sort_tup(a):
    return tuple(sorted(a))

def ind(s1,s2):
    look_up = dict()

    retrive = dict()

    len_digit = {
            2:1,
            4:4,
            3:7,
            7:8
            }


    s1_list = [a for a in s1.split(" ") if a not in [" ",""]]
    s2_list = [a for a in s2.split(" ") if a not in [" ",""]]

    for s in s1_list:
        # find 1,4,7,8
        s = set(s)

        if len(s) in len_digit:
            retrive[len_digit[len(s)]] = s 
    
    s1_list =remove_digits(s1_list,retrive)

    for s in s1_list:

        s = set(s)

        if (len(s) == 6) and len(retrive[1]-s) == 1:
            retrive[6] = s
        elif (len(s) == 6) and len(s - (retrive[4] | retrive[7])) == 1:
            retrive[9] = s
        elif len(s) == 6:
            retrive[0] = s
        elif len(retrive[1]-s) == 1 and len(retrive[4] - s) == 1:
            retrive[5] = s
        elif len(retrive[1]-s) == 1 and len(retrive[4] - s) == 2:
            retrive[2] = s
        elif len(retrive[1] - s) == 0:
            retrive[3] = s
    
    digit_str = ""

    for digit in s2_list:
        for key in retrive:
            if set(digit) == retrive[key]:
                digit_str = digit_str + str(key)
            
    return int(digit_str)

        

def test():
    file = open("report","r")

    total = 0
    
    line = file.readline()

    file.close()

    s1,s2 = line.split("|")
    s2 = s2[:-1]

    print(s1,s2,ind(s1,s2))



def part1():
    file = open("report","r")
    
    total = 0

    for line in file:
        s1,s2 = line.split("|")

        s2 = s2[:-1]
        
        total += find_1478(s2)
        
    file.close()
    print(total)

def part2():

    file = open("report","r")

    total = 0

    for line in file:
        s1,s2 = line.split("|")
        s2 = s2[:-1]

        total += ind(s1,s2)


    file.close()

    #print(total)

if __name__ == "__main__":
    print("Part1: ", end = "")
    part1()
    print("Part2: ", end = "")
    part2()

    #test()
