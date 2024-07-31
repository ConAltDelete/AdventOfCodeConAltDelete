package main

import(
	"os"
	"strconv"
	"bufio"
)

func part1(report [][]int) {
	
	var transpose = make([][]int, len(report[0]))
	
	for i := range transpose {
		var row = make([]int, len(report))
		transpose[i] = row
	}

	for i, line := range report {
		for j, val := range line {
			transpose[j][i] = val
		}
	}

	var gamma int64 = 0
	var total int = 0

	var length int = len(transpose[0])

	for _, line := range transpose {
		total = 0
		gamma <<= 1
		for _, n := range line {
			total += n
		}
		if total > length/2 {
			gamma += 1
		}
	}

	print(gamma * int64( gamma ^ ( 1<<len(transpose) - 1) ))


}

func part2(report [][]int) {
	/*
	PLAN:
	
	1) indexen av v,e kan kalkuleres samtidig men vi kan redusere ved å sette index til -1 som aldri blir brukt
	2) hent alle riktige indexer

	*/

	var index int = 0

	var gamma bool = false
	var epsilon bool = false
	
	var gamma_index = make([]int,len(report))
	var epsilon_index = make([]int,len(report))
	
	for i := 0; i < len(report); i++ {
		gamma_index[i] = i
		epsilon_index[i] = i
	}

	var gam_common int = 0
	var epsi_lest int = 0
	
	var total_gam int = 0
	var total_eps int = 0

	for index < len(report[0]) && (!gamma || !epsilon) { // inf loop

		for i, line := range report {
			if gamma_index[i] > -1 {
				total_gam += 1
				gam_common += line[index]
			}
			if epsilon_index[i] > -1 {
				total_eps += 1
				epsi_lest += line[index]
			}
			
		}

		if gam_common >= total_gam/2 { gam_common = 1 } else {gam_common = 0}
		if epsi_lest > total_eps/2 { epsi_lest = 0 } else { epsi_lest = 1}
		
		for i := 0; i < len(report); i++ {
			if report[i][index] != gam_common {
				gamma_index[i] = -1
			}

			if report[i][index] != epsi_lest {
				epsilon_index[i] = -1
			}
		}
		


		index += 1
	}

}

func main() {

	bits := [][]int{}

	file, err := os.Open("report")

	if err != nil {
		print(err.Error() + "\n")
		os.Exit(1)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	var str string = ""

	for scanner.Scan() {
		str = scanner.Text()
		var list_bit = make([]int, len(str))
		for i := 0; i < len(str); i++ {
			list_bit[i], err = strconv.Atoi(string(str[i]))
		}
		bits = append(bits, list_bit)
	}

	print("part 1: ")
	part1(bits)
	print("\nPart 2: ")
	part2(bits)
}
