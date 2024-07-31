package main

import (
	"strings"
	"strconv"
	"io/ioutil"
)

func part1(file string) {
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	data := strings.Split(string(bytes), "\r\n")
	data = data[:len(data)-1]
	
	data_int := make([]int, 0)

	for _, v := range data {
		value, err := strconv.Atoi(v)
		if err != nil {
			print(err.Error())
			return
		}
		data_int = append(data_int, value)
	}

	var i int = 0
	var steps int = 0

	var jump int
	for i < len(data_int) {
		jump = data_int[i]
		data_int[i] += 1
		i += jump
		steps++
	}
	print(steps)

}

func part2(file string) {
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	data := strings.Split(string(bytes), "\r\n")
	data = data[:len(data)-1]
	
	data_int := make([]int, 0)

	for _, v := range data {
		value, err := strconv.Atoi(v)
		if err != nil {
			print(err.Error())
			return
		}
		data_int = append(data_int, value)
	}

	var i int = 0
	var steps int = 0

	var jump int
	for i < len(data_int) {
		jump = data_int[i]
		if jump >= 3 {
			data_int[i] -= 1
		} else {
			data_int[i] += 1
		}
		i += jump
		steps++
	}
	print(steps)

}

func main() {
	print("Part 1: ")
	part1("input")
	print("\nPart 2: ")
	part2("input")
	print("\n")
}
