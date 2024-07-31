package main

import(
	"os"
	"strconv"
	"strings"
	"bufio"
)

type data struct {
	com string
	num int
}

func part1(commands []data) {
	var coords = map[string]int {
		"hor": 0,
		"depth": 0,
	}
	
	for i := 0; i < len(commands); i++ {
		var n data = commands[i]
		switch n.com {
			case "up":
				coords["depth"] = coords["depth"] - n.num
			case "forward":
				coords["hor"] = coords["hor"] + n.num
			case "down":
				coords["depth"] = coords["depth"] + n.num
			default:
				print("Failed!\n")
		}
	}

	print(coords["hor"]*coords["depth"])
}

func part2(commands []data) {
	var coords = map[string]int {
		"hor": 0,
		"depth": 0,
		"aim": 0,
	}
	
	for i := 0; i < len(commands); i++ {
		var n data = commands[i]
		switch n.com {
			case "up":
				coords["aim"] = coords["aim"] - n.num
			case "forward":
				coords["hor"] = coords["hor"] + n.num
				coords["depth"] = coords["depth"] + coords["aim"]*n.num
			case "down":
				coords["aim"] = coords["aim"] + n.num
			default:
				print("Failed!\n")
		}
	}

	print(coords["hor"]*coords["depth"])
}

func main() {
	input, err := os.Open("commands")
	if err != nil {
		print("Did not read!")
		os.Exit(1)
	}
	var commands []data
	
	scanner := bufio.NewScanner(input)

	for scanner.Scan() {
		text := strings.Split(scanner.Text(), " ")
		num, _ := strconv.Atoi(text[1])
		value := data{text[0], num}
		commands = append(commands, value)
	}
	
	print("part 1: ")
	part1(commands)
	print("\npart 2: ")
	part2(commands)
}
