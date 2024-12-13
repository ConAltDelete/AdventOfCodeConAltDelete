package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func main() {
	file, ok := os.Open("input")
	if ok != nil {
		panic("Could not find file!")
	}
	file_scann := bufio.NewScanner(file)

	var mapping [][]int = make([][]int, 0)
	var conv_line []int = make([]int, 0)
	P1_map := new(Mountain_map)
	for file_scann.Scan() {
		line := file_scann.Text()
		conv_line = []int{}
		for _, L := range line {
			l, ok := strconv.Atoi(L)
			if ok != nil {
				log.Printf("Could not convert '%v' to int", L)
			}
			conv_line = append(conv_line, l)
		}
		mapping = append(mapping, conv_line)
	}
	P1_map.int_map = mapping

}
