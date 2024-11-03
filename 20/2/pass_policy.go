package main

import "strings"

type Policy struct { // dictates minimum and maximum number of uses a letter has to be used
	min, max int
	letter   rune
}

func (Pol Policy) Pass_validation_old(pass string) bool {
	// validates password based on policy
	count := strings.Count(pass, string(Pol.letter))
	if Pol.min <= count && count <= Pol.max {
		return true
	}
	return false
}

func (Pol Policy) Pass_validation_new(pass string) bool {
	// validates password based on policy
	letter_test_p1 := pass[Pol.min-1] == byte(Pol.letter)
	letter_test_p2 := pass[Pol.max-1] == byte(Pol.letter)
	return letter_test_p1 != letter_test_p2
}
