package main

import (
	"bufio"
	"os"
	"slices"
	"strconv"
)

func main() {
	file, ok := os.Open("./input")

	if ok != nil {
		panic("Could not read file!")
	}

	reader := bufio.NewScanner(file)

	var expenses []int = []int{}

	var line string
	for reader.Scan() {
		// assume int value
		line = reader.Text()

		s2i, ok := strconv.Atoi(line)
		if ok != nil {
			panic("String '" + line + "' could not convert!")
		}
		expenses = append(expenses, s2i)
	}

	slices.Sort(expenses)

	var (
		start, mid, end int = 0, 0, len(expenses) - 1
		exp_sum         int
		exp_mid_sum     int
	)

	for start != end {
		exp_sum = expenses[start] + expenses[end]
		if exp_sum == 2020 {
			println("Found it! Part 1:")
			println(expenses[start] * expenses[end])
			break
		} else if exp_sum > 2020 {
			end--
		} else if exp_sum < 2020 {
			start++
		}
	}

	start, end = 0, len(expenses)-1

	for expenses[start]+expenses[end] > 2020 {
		end--
	}

	for start != end {
		exp_sum = expenses[start] + expenses[end]
		for mid = start + 1; mid < end; mid++ {
			exp_mid_sum = exp_sum + expenses[mid]
			if exp_mid_sum > 2020 {
				end--
				break
			} else if exp_mid_sum == 2020 {
				println("Found it! Part 2:")
				println(expenses[start] * expenses[mid] * expenses[end])
				os.Exit(0)
			}
		}
		if exp_mid_sum < 2020 {
			start++
		}
		// did not find a valid sum
	}
	println("Did not find it!")
}
