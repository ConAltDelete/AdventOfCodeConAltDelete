STAND_TYP_VALTYP = {
    "byr":(1920,2002),
    "iyr":(2010,2020),
    "eyr":(2020,2030),
    "hgt":({"cm":150,"in":59},{"cm":193,"in":76}),
    "hcl":(None),
    "ecl":("amb","blu","brn","gry","grn","hzl","oth"),
    "pid":(None,None),
    "cid":(None,None)
}


import io
import logging as lg
import re

lg.basicConfig(filename='advent.4.log', filemode="w", level=lg.INFO)

class passport:
    def __init__(self, informasjon: dict) -> None:
        lg.info("Initilisd objeckt with info:" + str(informasjon))
        self.info: dict = informasjon
        self.valid = self.self_validate()

    def self_validate(self) -> bool:
        # Returns True if ok, else False
        word_list = set(self.info.keys())
        must_list = set(STAND_TYP_VALTYP.keys()) - {"cid"}
        exclusive_list = word_list ^ must_list
        lg.info("Calculated lists inside objekt; word:{} ^ must:{} -> exclusive:{}".format(word_list,must_list,exclusive_list))
        
        if not(exclusive_list == set() or exclusive_list == {"cid"}):
            return False
        
        for K in word_list:
            if not self.validate_type(K):
                lg.info("Value {}:{} was not correct".format(K,self.info[K]))
                return False
        return True

    def validate_type(self,type2check: str) -> bool:
        lg.info("Validating Value: {}:{}".format(type2check,self.info[type2check]))
        match type2check:
            case "pid":
                return len(self.info["pid"]) == 9 and self.info["pid"].isnumeric()
            case "byr":
                rang: tuple[int,int] = STAND_TYP_VALTYP["byr"]
                return rang[0] <= int(self.info["byr"]) <= rang[1]
            case "iyr":
                rang: tuple[int,int] = STAND_TYP_VALTYP["iyr"]
                return rang[0] <= int(self.info["iyr"]) <= rang[1]
            case "eyr":
                rang: tuple[int,int] = STAND_TYP_VALTYP["eyr"]
                return rang[0] <= int(self.info["eyr"]) <= rang[1]
            case "ecl":
                return self.info["ecl"] in STAND_TYP_VALTYP["ecl"]
            case "hgt": # treat 'cm' and 'in' different
                if "in" not in self.info["hgt"] and "cm" not in self.info["hgt"]:
                    return False
                num, unit = self.info["hgt"][:-2],self.info["hgt"][-2:]
                return STAND_TYP_VALTYP["hgt"][0][unit] <= int(num) <= STAND_TYP_VALTYP["hgt"][1][unit]
            case "hcl":
                return len(self.info["hcl"]) == 7 and (re.fullmatch("#[0-9a-f]{6}",self.info["hcl"]) is not None)
            case "cid": # ignore
                return True
            case _:
                lg.warning("Unknown field :{}".format(type2check))


def val2int(strval:str) -> int | bool:
    match strval[0]:
        case "#": # hex
            return int(strval[1:],base=16)
        case "0": # octal
            return int(strval[1:], base=8)
        case _:
            lg.warning("Value without known base:" + strval + "; Returns False.")
            return False

def file_seeker(file: io.FileIO, new_newline: str):
    string_buffer = ""
    buffer_size = 0
    buffer_size_MAX = 10_000
    for line in file:
        lg.info("Current code line: '" + str([ord(letter) for letter in line]) +"'")
        if line == "\n": #! assumes that there are no header line that are blank!
            lg.info("Found empty line. scope variables:{}".format(locals()))
            yield string_buffer.strip()
            string_buffer = ""
            buffer_size = 0
        buffer_size += len(line[:-1]) + 1
        lg.info("New line fetched. Current buffer size:" + str(buffer_size))
        string_buffer += line[:-1] + " "
        if buffer_size > buffer_size_MAX:
            lg.fatal("Buffer size past limit")
            raise ValueError("Can't find newline!")

if __name__ == "__main__":
    n_valid = -1
    n_valid_p2 = 0
    for line in file_seeker(open("input","r"), new_newline=r"\r\n\r\n"):
        if n_valid < 0:
            n_valid = 0
        word_list = {sep_line.split(":")[0]
                     for sep_line in line.split(" ")}
        must_list = set(STAND_TYP_VALTYP.keys()) - {"cid"}
        exclusive_list = word_list ^ must_list
        lg.info("Calculated lists; word:{} ^ must:{} -> exclusive:{}".format(word_list,must_list,exclusive_list))
        if exclusive_list == set() or exclusive_list == {"cid"}:
            n_valid += 1
            temp_passport = passport(
                {sep_line.split(":")[0]:sep_line.split(":")[1]
                     for sep_line in line.split(" ")}
            )
            if temp_passport.valid:
                n_valid_p2 += 1
        

    print("Part 1:", n_valid)
    print("Part 2:", n_valid_p2)
