package main

import (
	"io/ioutil"
	"strings"
	"strconv"
)

func array_print(A [16]int) {
	print("[")
	for _,v := range A {
		print(v,",")
	}
	print("]\n")
}

func dist(block [16]int) [16]int {
	var new_block [16]int

	var max_index int = 0

	for i := range block {
		if block[i] > block[max_index] {
			max_index = i
		}
	}

	var cargo int = block[max_index]
	block[max_index] = 0

	for i,v := range block {
		new_block[i] = v
	}

	for cargo > 0 {
		max_index = (max_index + 1)%16
		new_block[max_index] += 1
		cargo -= 1
	}
	/*
	array_print(block)
	array_print(new_block)
	*/
	return new_block
}

func part1(file string) {
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	data := strings.Split(string(bytes),"\r\n")
	data = data[:len(data)-1]

	var blocks [16]int 

	for i, v := range strings.Split(data[0],"\t") {
		value, err := strconv.Atoi(v)
		if err != nil {
			print(err.Error())
			return
		}
		blocks[i] = value
	}

	dict := make(map[[16]int]bool,0)

	var ok bool = true
	var cycle int = 0
	
	for {
		cycle++
		// array_print(blocks)
		blocks = dist(blocks)
		_, ok = dict[blocks]
		if ok {
			print(cycle)
			return
		}
		dict[blocks] = true
	}	
}

func part2(file string) {
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	data := strings.Split(string(bytes),"\r\n")
	data = data[:len(data)-1]

	var blocks [16]int 

	for i, v := range strings.Split(data[0],"\t") {
		value, err := strconv.Atoi(v)
		if err != nil {
			print(err.Error())
			return
		}
		blocks[i] = value
	}

	dict := make(map[[16]int]bool,0)

	var ok bool = true
	var cycle int = 0

	var cycle_rep [16]int
	var found bool = false
	
	for {
		cycle++
		// array_print(blocks)
		blocks = dist(blocks)
		_, ok = dict[blocks]
		if ok && !found {
			found = true
			cycle_rep = blocks
			cycle = 0
		} else if ok && found && blocks == cycle_rep {
			print(cycle)
			return
		}
		dict[blocks] = true
	}	
}

func main() {
	print("Part 1: ")
	part1("input")
	print("\nPart 2: ")
	part2("input")
	print("\n")
}
