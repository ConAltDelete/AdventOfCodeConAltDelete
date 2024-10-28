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
	empt_poli := new(Policy)

	min, ok_1 := strconv.Atoi(tolkens[0])
	max, ok_2 := strconv.Atoi(tolkens[0])

	// 3. compose components

	if ok_1 != nil || ok_2 != nil {
		return "", *empt_poli, errors.New("Could not convert numbers")
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
		line, pass    string
		poly          Policy
		pass_ploy     *Pass_poly
		pass_poly_arr []Pass_poly
		valid_count   int = 0
	)

	for reader.Scan() {
		line = reader.Text()
		pass, poly, ok = parse_line2policy(line)
		if ok != nil {
			panic("paring went wrong!")
		}
		pass_ploy = new(Pass_poly)
		pass_ploy.pass = pass
		pass_ploy.policy = poly
		pass_poly_arr = append(pass_poly_arr, *pass_ploy)

		if poly.Pass_validation(pass) {
			valid_count++
		}
	}
	count_str := strconv.Itoa(valid_count)
	println("Finnished parsing. Final count: " + count_str)
}
