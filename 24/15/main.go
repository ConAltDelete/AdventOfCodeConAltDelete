package main

import (
	"bufio"
	"log"
	"os"
)

func main() {
	file, ok := os.Open("input")

	if ok != nil {
		log.Fatal(ok)
		panic("Could not open file")
	}

	defer file.Close()

	log_file, err := os.Create("./advent.24.15.log")

	if err != nil {
		log.Fatal(err)
	}

	log.SetOutput(log_file)
	log.SetFlags(log.Lshortfile | log.Ldate | log.Ltime)

	// first fine meta data, then data
	file_read := bufio.NewReader(file)

	Scanner := bufio.NewScanner(file_read)

	var (
		varehus Warehouse
		y       int = 0
	)

	for Scanner.Scan() {
		// stop when new_line
		line := Scanner.Text()

		if line == "" {
			break
		}

		flooring, fish := map_line(y, line)

		if fish != nil {
			varehus.lanternfish = fish
		}

		varehus.plantegning = append(varehus.plantegning, flooring)
		y++
	}

	digitaliser_varehus(&varehus)

	for Scanner.Scan() {
		commands := Scanner.Text()

		simulate_robot(&varehus, commands)

	}

	coord_sum = 0

	for i := range varehus.plantegning {
		for j := range varehus.plantegning[0] {
			value := varehus.plantegning[i][j]
			if value == BOX {
				coord_sum += GPS_coord([2]int{j, i})
			}
		}
	}

	println(coord_sum)

}
