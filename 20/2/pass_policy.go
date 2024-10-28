package main

import "strings"

type Policy struct { // dictates minimum and maximum number of uses a letter has to be used
	min, max int
	letter   rune
}

func (Pol Policy) Pass_validation(pass string) bool {
	// validates password based on policy
	count := strings.Count(pass, string(Pol.letter))
	if Pol.min <= count && count <= Pol.max {
		return true
	}
	return false
}
