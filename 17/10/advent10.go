package main

import (
	"io/ioutil"
	"strconv"
	"strings"
)

type circ_list struct {
	index int
	value int
	next *circ_list
	pre *circ_list
}

func (list circ_list) init(length int) *circ_list {
	
	var current *circ_list = &circ_list{
		index: 0,
		value: 0,
		next: nil,
		pre: nil,
	}

	var first *circ_list = current

	for i:=0; i<length; i++ {
		current.next = &circ_list{
			index: current.index + 1,
			value: current.value + 1,
			next: nil,
			pre: current,
		}
		current = current.next
	}
	
	current.next = first
	first.pre = current

	current = current.GetIndex(0)

	return current
}

func (list *circ_list) Reverse(length int) {
	var values = []int{list.value}

	var current *circ_list = list

	for i := 0; i < length; i++ {
		current = current.next
		values = append(values, current.value)
	}

	for i, j := 0, len(values)-1; i < j; i, j = i+1, j-1 {
		values[i], values[j] = values[j], values[i]
	}

	current = list
	
	for i := 0; i < length; i++ {
		current.value = values[i]
		current = current.next
	}
}

func (list *circ_list) GetIndex(i int) *circ_list {
	if list.index == i {
		return list
	} else if list.index > i {
		var temp *circ_list = list.pre

		for temp.index != list.index {
			if temp.index == i {
				return temp
			} else {
				temp = temp.pre
			}
		}
		return nil

	} else if list.index < i {
		var temp *circ_list = list.next

		for temp.index != list.index {
			if temp.index == i {
				return temp
			} else {
				temp = temp.next
			}
		}
		return nil

	}

	return nil
}

func part1(file string) {
	bytes, file_ok := ioutil.ReadFile(file)

	if file_ok != nil {
		print(file_ok.Error())
		return
	}

	list_str := strings.Split(string(bytes),",")
	list_str = list_str[:len(list_str)-2] // windows quirk '\r\n'

	var current int = 0

	var (
		skip_size int
		value string
		length int64
		convert_error error
	)

	list := new(circ_list)

	list = list.init(256)

	for skip_size,value = range list_str {
		length, convert_error = strconv.ParseInt(value,10,0)

		if convert_error != nil {
			print(convert_error.Error())
			return
		}
		
		list = list.GetIndex(current)
		
		list.Reverse(int(length))

		current += skip_size + int(length)

		current %= 256
	}
	
	list = list.GetIndex(0)

	if list == nil {
		print("Failed to get list\n")
		return
	}

	print(list.value * list.next.value)
}

func part2(file string) {}

func main() {
	print("Part 1: ")
	part1("input")
	print("\nPart 2: ")
	part2("input")
	print("\n")
}
