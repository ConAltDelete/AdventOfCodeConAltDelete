package main

import (
	"io/ioutil"
	"strings"
	"reflect"
)

func part1(file string) {
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	data_string := string(bytes)
	data := strings.Split(data_string,"\r\n")

	data = data[:len(data)-1]

	var dud bool

	var total int = 0

	for _, line := range data {
		dict := make(map[string]bool) 
		dud = false
		for _, word := range strings.Split(line ," ") {
			_, exist := dict[word]
			if exist {
				dud = true
				break
			}
			dict[word] = true
		}
		if dud {
			continue
		}

		total += 1
		
	}
	print(total)
}

func word2map(word string) map[rune]int {
	var ret = make(map[rune]int,0)

	for _, char := range word {
		_, ok := ret[char]
		if ok {
			ret[char] += 1
		} else {
			ret[char] = 1
		}
	}
	return ret
}

func part2(file string) {
	// Noe er galt. Må få mindre enn  383, men får 512...
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	data_string := string(bytes)
	data := strings.Split(data_string,"\r\n")

	data = data[:len(data)-1]

	var dud bool

	var total int = 0
	var gram map[rune]int

	for _, line := range data {
		dict := make([]map[rune]int,0)
		dud = false
		// print("line: ",line,"\n")
		for _, word := range strings.Split(line ," ") {
			gram = word2map(word)
			/* print("\tword: ",word,"\n")
			for key, val := range gram {
				print("\t\t",key, ":", val, "\n")
			}
			*/
			for _, sample := range dict {
				if reflect.DeepEqual(sample, gram) {
					// print("\t\tDud found!\n")
					dud = true
					break
				}
			}
			dict = append(dict, gram)
			if dud {
				break
			}
		}
		if dud {
			continue
		}
		total += 1
	}
	print(total)
}


func main() {
	print("Part 1: ")
	part1("input")
	print("\nPart 2: ")
	part2("input")
	print("\n")
}
