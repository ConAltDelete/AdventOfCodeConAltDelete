package main

import (
	"os"
	"strings"
	"bufio"
	"strconv"
	"slices"
	"unicode"
)

var num_list map[string]string = map[string]string{
	"one":"1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9",
}

func is_overlap()

func String_to_num(line string) string {
	/*
		Convert []string to a []string where numerics that are spelled out gets counted as numbers.

		notes:
			hvis et tall er "uforsturret" kan den trygt bli erstattet
			ellers finn alle tall i overlappet og set dem opp sekvensielt
	*/

	list_index := make(map[string]int,0)
	num_list_string := make([]string,0)
	for sn, _ := range num_list {

	}

	slices.SortFunc(num_list_string, func(i,j string)int{
		if list_index[i] < list_index[j] {
			return -1
		} else if list_index[i] == list_index[j] {
			return 0
		} else {
			return 1
		}
	})

	return string,string
}

func main() {
	path, err := os.Open(os.Args[1])

	if err != nil {
		panic("Could not open file")
	}
	File := bufio.NewScanner(path)

	sum := 0

	for File.Scan() {
		line := File.Text()
		lineF, lineB := String_to_num(line)
		h := strings.IndexFunc(lineF,func(L rune)bool{return unicode.IsNumber(L)} )
		t := strings.LastIndexFunc(lineB,func(L rune)bool{return unicode.IsNumber(L)} )
		num, err := strconv.Atoi(string(lineF[h]) + string(lineB[t]))
		if err != nil {
			panic("something happend with: " + string(lineF[h]) + string(lineB[t]))
		}
		sum += num
		print(line," ",num," ",sum,"\n")
	}

	print(sum,"\n")
}
