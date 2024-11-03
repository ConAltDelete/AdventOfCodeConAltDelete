package main

type coord struct {
	x     int
	y     int
	width int // limiter
	hight int // limiter
}

func change_coord(start coord, vector coord) (coord, coord, bool) {
	new_vec_y := 0
	reflection := false
	if start.y+vector.y >= start.hight {
		new_vec_y = 2*(start.hight-1) - (vector.y + start.y)
		vector.y *= -1
		reflection = true
	} else if start.y+vector.y < 0 {
		new_vec_y = -(start.y + vector.y) // sum is neg -> negate to get in range
		vector.y *= -1
		reflection = true
	} else {
		new_vec_y = start.y + vector.y
	}
	new_point := coord{
		x:     (start.x + vector.x) % start.width, // infinite left travel
		y:     new_vec_y,
		width: start.width,
		hight: start.hight,
	}

	return new_point, vector, reflection
}

func GCD(v coord) int {
	var (
		a, b int = v.y, v.x
	)

	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func count_tree_nonref(frame [][]bool, start coord, vect coord) int {
	var (
		n_points int
		reflect  bool
	)
	if n := GCD(vect); n > 1 { // coprime assurence
		vect.x /= n
		vect.y /= n

	}
	for vect.y < start.hight {
		start, vect, reflect = change_coord(start, vect) // overwrites vect due to reflection, needs to be changed.
		if reflect {
			break
		}
		if frame[start.y][start.x] { // there is a tree
			n_points += 1
		}
	}
	return n_points
}
