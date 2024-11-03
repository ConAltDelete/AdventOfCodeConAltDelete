package main

import (
	"bufio"
	"os"
)

func str2boolarr(line string) []bool {
	var bool_array []bool = make([]bool, len(line))
	for i, L := range line {
		bool_array[i] = L == '#'
	}
	return bool_array
}

func main() {
	file, ok := os.Open("./input")
	if ok != nil {
		panic("File not found!")
	}
	reader := bufio.NewScanner(file)

	var mini_map [][]bool = make([][]bool, 0)

	for reader.Scan() {
		line := reader.Text()
		bool_array := str2boolarr(line)
		mini_map = append(mini_map, bool_array)
	}
	start_point := coord{
		x:     0,
		y:     0,
		width: len(mini_map[0]),
		hight: len(mini_map),
	}
	vector := coord{
		x:     3,
		y:     1,
		width: -1,
		hight: -1,
	}
	p1 := count_tree_nonref(mini_map, start_point, vector)

	println("Part 1: Counted trees: ", p1)

	var (
		p2                int     = 1
		acceptible_angles []coord = []coord{
			{x: 1, y: 1, width: -1, hight: -1},
			{x: 3, y: 1, width: -1, hight: -1},
			{x: 5, y: 1, width: -1, hight: -1},
			{x: 7, y: 1, width: -1, hight: -1},
			{x: 1, y: 2, width: -1, hight: -1},
		}
	)
	for _, ang := range acceptible_angles {
		p2 *= count_tree_nonref(mini_map, start_point, ang)
	}
	println("Part 2: mutiplied trees: ", p2)
}
