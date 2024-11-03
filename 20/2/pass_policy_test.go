package main

import (
	"testing"
)

func TestParse(t *testing.T) {
	test_line := "1-3 a: abcde"
	password, policy, ok := parse_line2policy(test_line)

	if ok != nil {
		panic(ok.Error())
	}

	if password != "abcde" {
		t.Fatalf("Password did not parse correct: %s", password)
	}
	if policy.max != 3 || policy.min != 1 {
		t.Fatalf("Range failed: min->%v  max->%v", policy.min, policy.max)
	}
	if policy.letter != rune('a') {
		t.Fatalf("Letter failed: letter->%v", policy.letter)
	}

}

func TestPass_validation(t *testing.T) {
	test_policy := Policy{
		min:    1,
		max:    3,
		letter: 'a',
	}

	true_test := "abcde"  // true
	false_test := "aqagk" // false

	if test_policy.Pass_validation_new(true_test) != true {
		t.Errorf("Could not validate correct string")
	}
	if test_policy.Pass_validation_new(false_test) != false {
		t.Errorf("Could not invalidate false string")
	}
}
