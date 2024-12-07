package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func mult(a string, b string) (int, error) {
	a_conv, ok_a := strconv.Atoi(a)
	b_conv, ok_b := strconv.Atoi(b)

	if ok_a != nil || ok_b != nil {
		return -1, fmt.Errorf("Could not convert numbers: %v & %v", a, b)
	}

	return a_conv * b_conv, nil
}

func main() {
	file_ref, ok := os.Open("input")

	if ok != nil {
		panic("Could not find file")
	}

	file := bufio.NewScanner(file_ref)

	pattern := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))`)

	//groups := make([][]int, 0)
	var (
		prod_sum      int  = 0
		cond_prod_sum int  = 0
		mult_enabled  bool = true
	)

	for file.Scan() {
		line := file.Text()
		groups := pattern.FindAllStringSubmatch(line, -1)
		for _, g := range groups {
			mult_enabled = command_parser(g[0], mult_enabled)
			ab, ok := mult(g[1], g[2])
			if ok != nil {
				print(ok.Error())
				continue
			}
			prod_sum += ab
			if mult_enabled {
				cond_prod_sum += ab
			}

		}
	}

	fmt.Printf("Part 1: %v\n", prod_sum)
	fmt.Printf("Part 2: %v\n", cond_prod_sum)
}

func command_parser(command string, switchboard bool) bool {
	switch command {
	case "do()":
		return true
	case "don't()":
		return false
	default:
		return switchboard
	}
}
