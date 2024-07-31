package test

type coord struct {
	x int
	y int
}

func main() {
	var a coord = coord{0, 0}

	switch a {
		case a.x :
			print("1\n")
		case coord{0, _}:
			print("2\n")
		case coord{0, 0}:
			print("3\n")
		default:
			print("failed\n")
	}
	
}
