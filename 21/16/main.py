def fetch_packet(data, number = -1, count = -1):
    i = 0
    collection = []
    while i < len(data):
        pack = dict()

        pack["pv"] = int(data[i:i+3],2)
        pack["pt"] = int(data[i+3:i+6],2)

        i += 6

        if pack["pt"] == 4:
            num = ""
            while data[i] != "0":
                num += data[i+1:i+5]
                i += 5
            num += data[i+1:i+5]
            pack["data"] = int(num,2)
            i += 5
      
        else:
            L = data[i]
            i += 1

            if L == "0":
                I = int(data[i:i+15],2)
                i += 15
                subpack, inter_i = fetch_packet(data[i:],count = I)
                i += inter_i
                pack["data"] = subpack
            else:
                I = int(data[i:i+11],2)
                i += 11
                subpack, inter_i = fetch_packet(data[i:],number=I)
                i += inter_i
                pack["data"] = subpack

        collection.append(pack)
        if i%4 != 0:
            i += 4 - (i%4) 
        if count > -1:
            if i > count:
                break
        elif number > -1:
            if len(collection) >= number:
                break

    return collection, i




def part1():
    file = open("input","r")

    stream = file.readline()[:-1]
    file.close()

    binary = bin(int(stream,16))[2:]

    print(binary)
    
    data, _ = fetch_packet(binary)

    total = 0
    
    packets = data

    for pack in packets:
        total += pack["pv"]
        if pack["pt"] != 4:
            packets.extend(pack["data"])

    print(total)


def part2():
    pass #file = open("input","r")

if __name__ == "__main__":
	print("part 1: ",end="")
	part1()
	print("part 2: ",end="")
	part2()

