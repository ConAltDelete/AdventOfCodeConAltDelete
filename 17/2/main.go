package main

import (
	"io/ioutil"
	"strings"
	"math"
	"errors"
	"strconv"
)

func mum(A []int, sign int) (int, error) {
	if len(A) == 0 {
		return math.MaxInt, errors.New("Array eq 0")
	}

	if sign == 0 {
		sign = 1
	}
	
	var small int

	if sign < 0 {
		small = math.MaxInt
	} else {
		small = math.MinInt
	}

	for _, a := range A {
		if (a > small && sign > 0) || (a < small && sign < 0) {
			small = a
		}
	}
	return small, nil
}

func part1(file string) {
	bytes, err := ioutil.ReadFile(file)

	if err != nil {
		print("File could not read.\n")
		return
	}

	var data string = string(bytes)
	split := strings.Split(data, "\r\n")
	split = split[:len(split)-1]
	
	var total int = 0

	for _, line := range split {
		var numbers = make([]int,0)
		for _, a := range strings.Split(line, "\t") {
			conv, err := strconv.Atoi(a)
			if err != nil {
				print("faild to convert number from string: ", a)
				return
			}
			numbers = append(numbers, conv)
		}
		max, err1 := mum(numbers,1)
		min, err2 := mum(numbers,-1)
		
		if err1 != nil || err2 != nil {
			print("Did not find max, or min")
			return
		}

		total += max-min
	}
	print(total)
}

func find_even_div(A []int) (int,int,error) {
	var length int = len(A)

	var max int
	var min int

	for i := 0; i < length; i++ {
		for j := i+1; j < length; j++ {
			max = int(math.Max(float64(A[i]),float64(A[j])))
			min = int(math.Min(float64(A[i]),float64(A[j])))
			if max % min == 0 {
				return max, min, nil
			}
		}
	}

	return -1,-1,errors.New("Did not find divide.")
}

func part2(file string) {
	bytes, err := ioutil.ReadFile(file)

	if err != nil {
		print("File could not read.\n")
		return
	}

	var data string = string(bytes)
	split := strings.Split(data, "\r\n")
	split = split[:len(split)-1]
	
	var total int = 0
	var numbers = make([]int,0)
	
	for _, line := range split {
		numbers = []int{}
		for _, a := range strings.Split(line, "\t") {
			conv, err := strconv.Atoi(a)
			if err != nil {
				print("faild to convert number from string: ", a)
				return
			}
			numbers = append(numbers, conv)
		}
		a,b,err := find_even_div(numbers)
		
		if err != nil {
			print(err.Error())
			return
		}
		total += a/b
	}
	print(total)
}

func main() {
	print("Part 1: ")
	part1("input")
	print("\nPart 2: ")
	part2("input")
	print("\n")
}
