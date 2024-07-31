package main

import(
	"os"
	"strconv"
	"bufio"
)

func part1(num []int) {

	

	var total int = 0

	var pre int = num[0]

	for _, v := range num {
		if v > pre {
			total = total + 1
		}
		pre = v
	}

	print(total)
}

func part2(num []int){
	var trip []int
	
	for i := 1; i < len(num)-1; i++ {
		trip = append(trip, num[i-1] + num[i] + num[i+1])
	}

	var total int = 0

	var pre int = trip[0]

	for _, v := range trip {
		if v > pre {
			total++
		}
		pre = v
	}

	print(total)

}

func main(){
	input, err := os.Open("report")
	if err != nil {
		print("Did not read!")
		os.Exit(1)
	}
	defer input.Close()
	
	num := []int{}

	scanner := bufio.NewScanner(input)
	
	for scanner.Scan() {
		val,_ := strconv.ParseInt(scanner.Text(), 10,0)
		num = append(num, int(val))
		// print( strconv.Itoa(int(val)) + "\n")
	}
	
	print("part 1: ")
	part1(num)
	print("\n")
	print("part 2: ")
	part2(num)

}
