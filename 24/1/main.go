package main

import (
	"bufio"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {

	Logger_file, ok := os.Create("adventLog.24.1.log")

	if ok != nil {
		panic("Logging file did not succed.")
	}

	log.SetOutput(Logger_file)

	log.SetFlags(log.Lshortfile | log.Ldate | log.Ltime)

	file_name := "input"

	File, ok := os.Open(file_name)

	if ok != nil {
		log.Fatal("Could not find file. File not found:" + file_name)
	}

	log.Print("Found the file without error.")

	scanner := bufio.NewScanner(File)

	var (
		left_array  []int
		right_array []int
		p_ints      [2]int
		line        string
	)

	for scanner.Scan() {
		line = scanner.Text()
		p_ints = parse_line(line)
		left_array = append(left_array, p_ints[0])
		right_array = append(right_array, p_ints[1])
	}

	left_array = SortInts(left_array)
	right_array = SortInts(right_array)

	var diff_sum float64 = 0

	for i := range left_array {
		diff_sum += math.Abs(float64(left_array[i] - right_array[i]))
	}

	println(int(diff_sum))
	println(count_sim(left_array, right_array))

}

func count_sim(left_array []int, right_array []int) int {
	right_array_hash := make(map[int]int)
	for _, el := range right_array {
		_, ok := right_array_hash[el]
		if !ok {
			right_array_hash[el] = 1
		} else {
			right_array_hash[el]++
		}
	}
	var counting int = 0
	for _, el := range left_array {
		count, ok := right_array_hash[el]
		if !ok {
			continue
		}
		counting += el * count
	}
	return counting
}

func parse_line(line string) [2]int {
	residual := strings.Split(line, "   ") // get two str
	if len(residual) > 2 {
		log.Printf("Found %v rather than 2. Proseeds assuming 2.", len(residual))
	}

	var ret_arr [2]int

	for i := range residual {
		if i > 2 {
			break
		}
		parsed, ok := strconv.Atoi(residual[i])
		if ok != nil {
			log.Printf("Couldn't parse %v at position %v", residual[i], i)
			ret_arr[i] = -1
		}
		ret_arr[i] = parsed
	}

	return ret_arr

}

func SortInts(arr []int) []int {
	tree_arr := new(binTree)

	for _, el := range arr {
		tree_arr = insert(tree_arr, el)
	}

	sorted_arr := Tree2Array(*tree_arr)

	return sorted_arr
}
