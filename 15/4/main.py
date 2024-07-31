import hashlib

def part1():
    
    salt = open("input","r").readline()[:-1]

    i = 0
    result = "aaaaaaaaaa"

    lim = 100000000000000
    while result[:6] != "000000" and i < lim:
        key = salt + str(i)
        result = hashlib.md5(key.encode(encoding="utf8")).hexdigest()
        i += 1

    if i == lim:
        print("fail")
    else:
        print(salt,result,i-1)


part1()
