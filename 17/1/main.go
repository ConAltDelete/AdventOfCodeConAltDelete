package main

import (
	"io/ioutil"
	"os"
	"strings"
	"strconv"
)

func part1(file string) {
	bytes, err := ioutil.ReadFile(file)
	
	if err != nil {
		os.Exit(1)
	}

	innhold := string(bytes)
	split := strings.Split(innhold,"\n")

	split = split[:len(split)-1]
	
	
	total := 0
	for _,digit := range split {
		sub_total := 0
		digit = digit[:len(digit)-1]
		for i, c := range string(digit) {
			conv, err1 := strconv.Atoi(string(c))
			conv_n, err2 := strconv.Atoi(string(digit[(i+1)%len(digit)]))
			
			if err1 != nil || err2 != nil {
				if err1 == nil {
					print("ERROR 1:",c,"\n")
				}
				if err2 == nil {
					print("ERROR 2:",digit[(i+1)%len(digit)],"\n")
				}
				continue
			}
			
			if conv == conv_n {
				sub_total += conv
			}
		}
		total += sub_total
	}
	print(total)
}

func part2(file string) {
	bytes, err := ioutil.ReadFile(file)
	
	if err != nil {
		os.Exit(1)
	}

	innhold := string(bytes)
	split := strings.Split(innhold,"\n")

	split = split[:len(split)-1]
	
	total := 0
	var length int
	for _,digit := range split {
		sub_total := 0
		length = len(digit)/2
		digit = digit[:len(digit)-1]
		for i, c := range string(digit) {
			conv, err1 := strconv.Atoi(string(c))
			conv_n, err2 := strconv.Atoi(string(digit[(i+length)%len(digit)]))
			
			if err1 != nil || err2 != nil {
				if err1 == nil {
					print("ERROR 1:",c,"\n")
				}
				if err2 == nil {
					print("ERROR 2:",digit[(i+length)%len(digit)],"\n")
				}
				continue
			}
			
			if conv == conv_n {
				sub_total += conv
			}
		}
		total += sub_total
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
