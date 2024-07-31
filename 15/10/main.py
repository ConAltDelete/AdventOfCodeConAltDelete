def part1():
    file = open("input","r")

    string = file.readline()[:-1]

    array = [int(a) for a in string]

    for _ in range(40):
        new_array = []
        i = 0
        #breakpoint()
        letter = array[0]
        for char in array:
            if char == letter:
                i += 1
            else:
                new_array.append(i)
                new_array.append(letter)
                i = 1
                letter = char

        if i > 0:
            new_array.append(i)
            new_array.append(char)
        array = new_array
    print("length:",len(array))

def part2():
    file = open("input","r")

    string = file.readline()[:-1]

    array = [int(a) for a in string]

    for _ in range(50):
        new_array = []
        i = 0
        #breakpoint()
        letter = array[0]
        for char in array:
            if char == letter:
                i += 1
            else:
                new_array.append(i)
                new_array.append(letter)
                i = 1
                letter = char

        if i > 0:
            new_array.append(i)
            new_array.append(char)
        array = new_array
    print("length:",len(array))

    





part1()
part2()
