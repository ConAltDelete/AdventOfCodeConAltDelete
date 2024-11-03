package main

import (
	"bufio"
	"errors"
	"os"
	"strconv"
	"strings"
)

type Pass_poly struct {
	pass   string
	policy Policy
}

/*
Parsing string into a password [string] and a policy [Policy]

	returns an error if something is wrong
	assume: min-max letter: password
*/
func parse_line2policy(line string) (password string, policy Policy, ok error) {

	// 1. split string to components -> use strings.FieldFunc(s,rune func)
	var tolkens []string = strings.FieldsFunc(line, func(r rune) bool { return r == ':' || r == '-' || r == ' ' })
	// 2. identify components

	min, ok_1 := strconv.Atoi(tolkens[0])
	max, ok_2 := strconv.Atoi(tolkens[1])

	// 3. compose components

	empt_poli := new(Policy)

	if ok_1 != nil || ok_2 != nil {
		return "", *empt_poli, errors.New("could not convert numbers")
	}

	empt_poli.max = max
	empt_poli.min = min
	empt_poli.letter = rune(tolkens[2][0])
	password = tolkens[3]

	// 4. return respectible output

	return password, *empt_poli, nil

}

func main() {
	file, ok := os.Open("./input")
	if ok != nil {
		panic("Did not find file!")
	}

	reader := bufio.NewScanner(file)

	var (
		line, pass      string
		poly            Policy
		valid_count_old int = 0
		valid_count_new int = 0
	)

	for reader.Scan() {
		line = reader.Text()
		pass, poly, ok = parse_line2policy(line)
		if ok != nil {
			panic("paring went wrong!")
		}

		if poly.Pass_validation_old(pass) {
			valid_count_old++
		}

		if poly.Pass_validation_new(pass) {
			valid_count_new++
		}
	}

	println("Finnished parsing. Final count part 1: ", valid_count_old)
	println("Finnished parsing. Final count part 2: ", valid_count_new)
}
