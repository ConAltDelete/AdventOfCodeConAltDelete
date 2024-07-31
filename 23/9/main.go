package main


import (
	"strings"
	"bufio"
	"os"
	"strconv"
	"slices"
)

func check_all(seq []int) bool {
	for _,k := range seq {
		if k != 0 {
			return false
		}
	}
	return true
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	file_scann := bufio.NewScanner(file)

	p1_sum := 0
	p2_sum := 0

	for file_scann.Scan() {
		line_array := strings.Fields(file_scann.Text())
		line := make([]int,0)
		diff_map := make(map[int][]int,0)
		for _,n := range line_array {
			n_int, err := strconv.Atoi(n)
			if err != nil {
				panic("Something is wrong: " + n)
			}
			line = append(line, n_int)
		}
		diff_map[0] = line
		for i := 0; !check_all(diff_map[i]); i++ {
			// print(diff_map[i]," -> ")
			new_seq := make([]int,0)
			current_seq := diff_map[i]
			for i := 1; i < len(current_seq); i++ {
				new_seq = append(new_seq, current_seq[i] - current_seq[i-1])
			}
			diff_map[i+1] = new_seq
		}
		diff_map[len(diff_map)-1] = append(diff_map[len(diff_map)-1],0) // assumes all = 0
		for i := len(diff_map)-2; i >= 0; i-- {
			// bruker nye_element[i] = gamle_element[i] + nye_element[i+1]
			nedre_siste := diff_map[i+1][len(diff_map[i+1])-1]
			siste := diff_map[i][len(diff_map[i])-1]
			diff_map[i] = append(diff_map[i], nedre_siste + siste)
		}
		for i := len(diff_map)-2; i >= 0; i-- {
			// bruker nye_element[i] = gamle_element[i] + nye_element[i+1]
			nedre_siste := diff_map[i+1][0]
			siste := diff_map[i][0]
			diff_map[i] = slices.Insert(diff_map[i], 0, siste - nedre_siste)
		}
		// print(diff_map[0][len(diff_map[0])-1],"\n")
		p1_sum += diff_map[0][len(diff_map[0])-1]
		p2_sum += diff_map[0][0]
	}
	print(p1_sum,"\n")
	print(p2_sum,"\n")
}
