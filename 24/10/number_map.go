package main

type M_node struct {
	value        int
	previus_node []*M_node
	next_node    []*M_node
	path_score   int
	traversed    bool
}

type Mountain_map struct {
	score   int
	int_map [][]int
	Map     [][]*M_node
	mapped  bool
	size    [2]int
	tops    []*M_node
	bots    []*M_node
}

func conv_intMap2nodeMap(mapp *Mountain_map) {
	if mapp.mapped {
		return
	}
	mapp.size[0] = len(mapp.int_map[0])
	mapp.size[1] = len(mapp.int_map)

	for x := 0; x < mapp.size[0]; x++ {
		for y := 0; y < mapp.size[1]; y++ {
			curr_value := mapp.int_map[y][x]
			mapp.Map[y][x] = &M_node{
				value: curr_value,
			}
			if curr_value == 9 {
				mapp.tops = append(mapp.tops, mapp.Map[y][x])
			} else if curr_value == 0 {
				mapp.bots = append(mapp.bots, mapp.Map[y][x])
			}
		}
	}
}

func find_paths(mapp *Mountain_map) {
	if mapp.mapped {
		return
	}
	for x := 0; x < mapp.size[0]; x++ {
		for y := 0; y < mapp.size[1]; y++ {
			find_path(mapp, x, y)
		}
	}
}

func find_path(mapp *Mountain_map, x int, y int) {
	if mapp.Map[y][x].traversed {
		return
	}
	// Find trail

	var stack [][2]int = [][2]int{
		{x, y},
	}
	var point [2]int
	var neighborhood [][2]int
	for len(stack) > 0 {
		point = stack[len(stack)-1]
		curr_point := mapp.Map[point[y]][point[x]]
		stack = stack[0 : len(stack)-2]

		neighborhood = points_around(mapp, point)

		if neighborhood == nil {
			continue
		}
		for _, next_point := range neighborhood {
			curr_point.next_node = append(curr_point.next_node,
				mapp.Map[next_point[1]][next_point[0]])
			stack = append(stack, next_point)
		}
	}
}

func points_around(mapp *Mountain_map, point [2]int) [][2]int {
	value := mapp.int_map[point[1]][point[0]]
	if value == 9 {
		return nil
	}
	directions := [][2]int{
		{0, -1},
		{1, 0},
		{0, 1},
		{-1, 0},
	}
	ret_points := make([][2]int, 0)
	for _, point := range directions {
		if mapp.int_map[point[1]][point[0]]-value == 1 {
			ret_points = append(ret_points, point)
		}
	}
	return ret_points
}

func calc_score(x int, y int, mapp Mountain_map) {

}
