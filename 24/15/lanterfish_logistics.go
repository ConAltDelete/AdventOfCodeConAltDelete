package main

import "log"

const (
	AIR = iota
	BOX
	FISH
	WALL
)

var rune2object map[rune]int = map[rune]int{
	'#': WALL,
	'.': AIR,
	'@': FISH,
	'O': BOX,
}

type Fish struct {
	pos [2]int
}

type digital_Warehouse struct {
	row_array [][]*int
	col_array [][]*int
}

type Warehouse struct {
	plantegning         [][]int            // kartlegging
	digital_plantegning *digital_Warehouse // peker til indekser i plantegning
	lanternfish         *Fish
}

// Genererer digital_plantegning for simulering
func digitaliser_varehus(varehus *Warehouse) {
	var (
		row_array [][]*int
		col_array [][]*int = make([][]*int, len(varehus.plantegning[0]))
	)
	for i := range varehus.plantegning {
		var new_row []*int = make([]*int, 0)
		for j := range varehus.plantegning[0] {
			col_array[j] = append(col_array[j], &varehus.plantegning[i][j])
			new_row = append(new_row, &varehus.plantegning[i][j])
		}
		row_array = append(row_array, new_row)
	}
	dW := digital_Warehouse{
		row_array: row_array,
		col_array: col_array,
	}
	varehus.digital_plantegning = &dW
}

func GPS_coord(lanternfish [2]int) int {
	return 100*lanternfish[1] + lanternfish[0]
}

func map_line(y_coord int, line string) ([]int, *Fish) {
	var floor_plan []int
	var lanternfish *Fish = nil

	for i, R := range line {
		r := rune2object[R]
		if r == FISH { // If the fish is found, replace with AIR while storing it in the "varehus"
			lanternfish = &Fish{
				pos: [2]int{
					i, y_coord,
				},
			}
			r = AIR // removes lanternfish and inserts air
		}
		floor_plan = append(floor_plan, r)
	}
	return floor_plan, lanternfish
}

func moveFish_1D(space []int, lanternfish int, command int) ([]int, int) {
	// command is +1 or -1 where -1 is backwards, and 1 is forward
	// lanternfish indicates the position of the fish
	// space is the 1D case

	var (
		new_space  []int
		peek_value int
	)

	new_space = append(new_space, space...)

	moved_fish := lanternfish + command

	peek_value = new_space[moved_fish]
	// check possibilities
	switch peek_value {
	case WALL:
		// Can't move
		return new_space, lanternfish // can't do anything anyways
	case BOX:
		// move box(es) one unit IF possible
		// need to check ahead
		k := moved_fish
		for new_space[k] == BOX {
			k += command
		}
		if new_space[k] == AIR {
			new_space[moved_fish] = AIR
			new_space[k] = BOX
		} else { // Has to be a WALL
			return new_space, lanternfish
		}
	}

	return new_space, moved_fish
}

func moveFish(varehus *Warehouse, command rune) {
	// positive y direction is downwards due to how the array gets filled.
	var movement_array []*int
	var direction int = +1
	var dimention int
	switch {
	case (command == '>') || (command == '<'):
		dimention = 0
		if command == '<' {
			direction = -1
		}
		movement_array = varehus.digital_plantegning.row_array[varehus.lanternfish.pos[1]]
	case (command == '^') || (command == 'v'):
		dimention = 1
		if command == '^' {
			direction = -1
		}
		movement_array = varehus.digital_plantegning.col_array[varehus.lanternfish.pos[0]]
	}

	var temp_space []int

	for _, v := range movement_array {
		temp_space = append(temp_space, *v)
	}

	temp_space, varehus.lanternfish.pos[dimention] = moveFish_1D(
		temp_space,
		varehus.lanternfish.pos[dimention],
		direction,
	)

	for i := range movement_array {
		*movement_array[i] = temp_space[i]
	}

}

// Simulerer robot bevegelse gjennom varehus
func simulate_robot(warehouse *Warehouse, commands string) {
	/* Strat:
	* 1) finn ut hvilke retning vi går -> rader eller kolloner
	* 2) bruk den digitale versjonen av varehuset til å gjøre transformasjoner
	* 3) skriv transformasjoner tilbake til addressene
	 */

	if warehouse.digital_plantegning == nil {
		log.Fatal("Varehus er ikke digitalisert!")
	}
	for _, com := range commands {
		moveFish(warehouse, com)
	}

}
