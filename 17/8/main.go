package main

import (
	"strings"
	"strconv"
	"io/ioutil"
	"math"
)

func part1(file string) {
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	var reg = make(map[string]int)

	var operand = map[string]func(string,int)bool {
		"==": func(a string, b int)bool{return reg[a] == b},
		"!=": func(a string, b int)bool{return reg[a] != b},
		"<=": func(a string, b int)bool{return reg[a] <= b},
		">": func(a string, b int)bool{return reg[a] > b},
		"<": func(a string, b int)bool{return reg[a] < b},
		">=": func(a string, b int)bool{return reg[a] >= b},
	}

	data := strings.Split(string(bytes),"\r\n")
	data = data[:len(data)-1]


	var command, cond []string
	var list []string

	for _, line := range data {
		list = strings.Split(line," if ")
		command = strings.Split(list[0]," ")
		cond = strings.Split(list[1]," ")

		bar, ok_bar := strconv.Atoi(string(cond[2]))
		change, ok_change := strconv.Atoi(string(command[2]))


		if ok_bar != nil {
			print(ok_bar.Error())
			return
		}
		if ok_change != nil {
			print(ok_change.Error())
			return
		}

		for _, r := range [2]string{command[0],cond[0]} {
			_, exist := reg[r]
			if !exist {
				reg[r] = 0
			}
		}

		if operand[cond[1]](cond[0],bar) {
			if command[1] == "inc" {
				reg[command[0]] += change
			} else {
				reg[command[0]] -= change
			}
		}
	}
	var maximum int = math.MinInt
	for _, value := range reg {
		if value > maximum {
			maximum = value
		}
	}
	print(maximum)
}

func part2(file string) {
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	var reg = make(map[string]int)

	var operand = map[string]func(string,int)bool {
		"==": func(a string, b int)bool{return reg[a] == b},
		"!=": func(a string, b int)bool{return reg[a] != b},
		"<=": func(a string, b int)bool{return reg[a] <= b},
		">": func(a string, b int)bool{return reg[a] > b},
		"<": func(a string, b int)bool{return reg[a] < b},
		">=": func(a string, b int)bool{return reg[a] >= b},
	}

	data := strings.Split(string(bytes),"\r\n")
	data = data[:len(data)-1]


	var command, cond []string
	var list []string

	var maximum int = math.MinInt

	for _, line := range data {
		list = strings.Split(line," if ")
		command = strings.Split(list[0]," ")
		cond = strings.Split(list[1]," ")

		bar, ok_bar := strconv.Atoi(string(cond[2]))
		change, ok_change := strconv.Atoi(string(command[2]))


		if ok_bar != nil {
			print(ok_bar.Error())
			return
		}
		if ok_change != nil {
			print(ok_change.Error())
			return
		}

		for _, r := range [2]string{command[0],cond[0]} {
			_, exist := reg[r]
			if !exist {
				reg[r] = 0
			}
		}

		if operand[cond[1]](cond[0],bar) {
			if command[1] == "inc" {
				reg[command[0]] += change
			} else {
				reg[command[0]] -= change
			}
			if reg[command[0]] > maximum {
				maximum = reg[command[0]]
			}
		}
	}
	print(maximum)
}

func main() {
	print("Part 1: ")
	part1("input")
	print("\nPart 2: ")
	part2("input")
	print("\n")
}
