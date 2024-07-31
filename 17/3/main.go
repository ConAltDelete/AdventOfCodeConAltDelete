package main

import (
	"io/ioutil"
	"strconv"
	"math"
)

func part1(file string){
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	number2eval, num_err := strconv.Atoi(string(bytes[:len(bytes)-2]))

	if num_err != nil {
		print(num_err.Error())
		return
	}
	
	var r int = int(math.Ceil(math.Sqrt(float64(number2eval))))
	
	if r % 2 == 0 {
		r += 1
	}

	r = int((r-1)/2)

	var numbers = make([]int,4)

	numbers[0] = int(math.Pow(float64(2*r+1),2)) - r

	for i := 1; i < 4; i++ {
		numbers[i] = numbers[i-1] - 2*r
	}

	for i := 0; i < 4; i++ {
		numbers[i] = int(math.Abs(float64(number2eval - numbers[i])))
	}

	var min int = math.MaxInt

	for i := 0; i < 4; i++ {
		if numbers[i] < min {
			min = numbers[i]
		}
	}
	
	print(r + min)


}

type coord struct {
	x int
	y int
}

func (c coord) add(b coord) coord {
	var ret coord
	ret.x = c.x + b.x
	ret.y = c.y + b.y
	return ret
} 

func get_coord(num int) coord {
	var r int = int(math.Ceil(math.Sqrt(float64(num))))
	
	if r % 2 == 0 {
		r += 1
	}

	r = int((r-1)/2)

	var convert = make(map[int]coord,4)
	var numbers = make([]int, 4)
	
	list := []coord{
		{0, -1*r},
		{-1*r,0},
		{0, r},
		{r,0},
	}

	convert[int(math.Pow(float64(2*r+1),2)) - r] = list[0]

	numbers[0] =int(math.Pow(float64(2*r+1),2)) - r 

	for i := 1; i < 4; i++ {
		numbers[i] = numbers[i-1] - 2*r
		convert[numbers[i]] = list[i]
	}


	var min int = math.MaxInt
	var min_coord coord
	var messure int
	var replace coord
	var check coord

	for i := 3; i > -1; i-- {
		messure = int(math.Abs(float64(num - numbers[i])))
		if messure < min {
			min = numbers[i]
			check = convert[min]
			if check.x == 0 && check.y > 0 {
				replace = coord{numbers[i] - num, 0}
			} else if check.x == 0 && check.y < 0 {
				replace = coord{num - numbers[i], 0}
			} else if check.y == 0 && check.x > 0 {
				replace = coord{0, num - numbers[i]}
			} else if (check.y == 0) && (check.x < 0) {
				replace = coord{0, numbers[i] - num}
			}
			min_coord = convert[min].add(replace)
			min = messure
		}
	}
	
	return min_coord
	
}

func get_around(mid coord) []coord {
	var list = []coord{
		{-1,  1}, {0,  1}, {1,  1},
		{-1,  0},          {1,  0},
		{-1, -1}, {0, -1}, {1, -1},
	}
	
	var ret = make([]coord,0)

	for i := range list {
		ret = append(ret, coord{mid.x + list[i].x, mid.y + list[i].y})
	}

	return ret
}

func part2(file string){
	bytes, file_err := ioutil.ReadFile(file)

	if file_err != nil {
		print(file_err.Error())
		return
	}

	number2eval, num_err := strconv.Atoi(string(bytes[:len(bytes)-2]))

	if num_err != nil {
		print(num_err.Error())
		return
	}
	
	grid := make(map[coord]int)

	grid[coord{0, 0}] = 1

	var current coord
	var around []coord
	var i int = 2
	var total int

	for {
		current = get_coord(i)
		around = get_around(current)
		
		total = 0

		for _, c := range around {
			value, cord_ok := grid[c]
			if !cord_ok {
				continue
			}
			total += value
		}

		
		if total > number2eval {
			print(total)
			return
		}
		
		grid[current] = total
		i++
	}

}

func main() {
	print("Part 1: ")
	part1("input")
	print("\nPart 2: ")
	part2("input")
	print("\n")
}
