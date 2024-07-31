package main

import (
	"strings"
	"strconv"
	"io/ioutil"
)

func part1(file string) {
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	data := strings.Split(string(bytes),"\r\n")
	data = data[:len(data)-1]

	var trees = make(map[string][]string)

	for _, d := range data {
		if strings.Contains(d,"->") {
			leftright := strings.Split(d, " -> ")
			name_list := strings.Split(leftright[0], " ")
			trees[name_list[0]] = strings.Split(leftright[1],", ")
		}
	}

	trees_copy := make(map[string][]string)

	for key, value := range trees {
		trees_copy[key] = value
	}

	for _, values := range trees_copy {
		for _, v := range values {
			_, exist := trees[v]
			if exist {
				delete(trees, v)
			}
		}
	}

	for v := range trees {
		print(v)
	}

}

type tree struct {
	name         string
	weight       int
	child_weight int
}

func (root tree) add(leafs ...tree) tree {
	for _, t := range leafs {
		root.child_weight += t.weight + t.child_weight
	}
	return root
}

func corrected(nodes map[string]tree, sample ...string) (int, bool) {
	/*
		Finne riktig vekt..
	*/
	count := make(map[int][]string, 0)

	var seed tree
	var total_weight int

	for _, value := range sample {
		seed = nodes[value]
		total_weight = seed.weight + seed.child_weight
		_, ok := count[total_weight]

		if ok {
			count[total_weight] = append(count[total_weight],value)
		} else {
			count[total_weight] = []string{value}
		}
	}

	if len(count) > 1 {
		unique := 0
		unique_str := ""
		other  := 0
		for key, values := range count {
			if len(values) == 1 {
				unique = key
				unique_str = values[0]
			} else if len(values) > 1 {
				other = key
			}
		}
		return (other - unique + nodes[unique_str].weight), true
	}

	return -1, false
}

func part2(file string) {
	/*
	Implementerer et tree, men må undersøke litt hvordan det skal fungere i go.
	Har konkludert at
		⮡ skal bruke depth-search ❌
		⮡ må implemntere et addering system ✅
		⮡ et verifiserings system. Ikke nødvendig lenger siden vi er bare ute etter vekt.

	Ideer:
		- konverter listen til en dict med string som nøkkel, og `tree` som value.
	*/
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	data := strings.Split(string(bytes),"\r\n")
	data = data[:len(data)-1]

	nodes := make(map[string]tree)
	connections := make(map[string][]string)

	for _, d := range data {
		if strings.Contains(d,"->") {
			leftright := strings.Split(d, " -> ")
			name_list := strings.Split(leftright[0], " ")
			w, num_err := strconv.Atoi(name_list[1][1:len(name_list[1])-1])
			if num_err != nil {
				print(num_err.Error())
				return
			}
			nodes[name_list[0]] = tree{
				name: name_list[0],
				weight: w,
			}
			connections[name_list[0]] = strings.Split(leftright[1],", ")
		} else {
			split_list := strings.Split(d, " ")
			w, num_err := strconv.Atoi(split_list[1][1:len(split_list[1])-1])
			if num_err != nil {
				print(num_err.Error())
				return
			}
			nodes[split_list[0]] = tree{
				name: split_list[0],
				weight: w,
			}
		}
	}


	for len(connections) > 0 {
		/*
			Det er noen tilfeller jeg må håndtere:
				1. Alle er blader
					⮡ legg dem sammen, og fjern den koblingen
				2. Noen, eller alle er trær
					⮡ ignorer, og finn neste tre
		*/

		for key, con := range connections {
			// case 2
			tree_flag := false
			for _, c := range con {
				_, ok := connections[c]
				if ok {
					tree_flag = true
					break
				}
			}
			if tree_flag {
				continue
			}

			// case 1, siden det er det eneste igjen
			
			// check if all weights are equal
			correct, changed := corrected(nodes,con...)	
			if changed {
				print(correct)
				return
			}
			
			// compress tree to a single node
			for _, c := range con {
				nodes[key] = nodes[key].add(nodes[c])
			}

			delete(connections,key) // removing connection
		}
	}
}

func main() {
	print("Part 1: ")
	part1("input")
	print("\nPart 2: ")
	part2("input")
	print("\n")
}
