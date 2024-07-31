package main

import (
	"io/ioutil"
)

func part1(file string) {
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	data_stream := string(bytes)
	data_stream = data_stream[:len(data_stream)-2]

	var stack = make([]string,0)
	var char string
	var points int = 0
	var last_bracket string
	
	stack = append(stack,string(data_stream[0]))

	for i := 1; i < len(data_stream); i++ {
		char = string(data_stream[i])
		last_bracket = stack[len(stack)-1]
		if char == "!" {
			i++
			continue
		} else if last_bracket == "<" && char == ">" {
			stack = stack[:len(stack)-1]
			continue
		} else if last_bracket == "<" {
			continue
		} else if stack[len(stack)-1] == "{" && char == "}" {
			points += len(stack)
			stack = stack[:len(stack)-1]
			continue
		}


		if char == "{" || char == "<" {
			stack = append(stack,char)
		}	
	}
	print(points)
}

func part2(file string) {
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	data_stream := string(bytes)
	data_stream = data_stream[:len(data_stream)-2]

	var stack = make([]string,0)
	var char string
	var points int = 0
	var last_bracket string
	
	stack = append(stack,string(data_stream[0]))

	for i := 1; i < len(data_stream); i++ {
		char = string(data_stream[i])
		last_bracket = stack[len(stack)-1]
		if char == "!" {
			i++
			continue
		} else if last_bracket == "<" && char == ">" {
			stack = stack[:len(stack)-1]
			continue
		} else if last_bracket == "<" {
			points++
			continue
		} else if stack[len(stack)-1] == "{" && char == "}" {
			stack = stack[:len(stack)-1]
			continue
		}


		if char == "{" || char == "<" {
			stack = append(stack,char)
		}	
	}
	print(points)
}

func main() {
	print("Part 1: ")
	part1("input")
	print("\nPart 2: ")
	part2("input")
	print("\n")
}
