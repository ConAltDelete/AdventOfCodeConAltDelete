package main

type binSubtree struct {
	value   int
	flag    bool
	parent  *binSubtree
	bigger  *binSubtree
	smaller *binSubtree
}

type binTree struct {
	mini *int
	maxi *int
	size int // number of nodes
	tree *binSubtree
}

func GetMin(main_tree binTree) int {
	return *main_tree.mini
}

func Tree2Array(main_tree binTree) []int {
	// inserts nodes to a array in order (min to max)
	// strat: 1) get to the left node (if exist),
	// 2) move to the right node if exist
	// 3) then move upwards to parent
	// 4) pretend you are now at the left node and start again.

	var (
		current_node *binSubtree
		ret_list     []int
		node_cue     []*binSubtree = []*binSubtree{main_tree.tree}
	)

	if main_tree.size == 1 {
		ret_list = append(ret_list, main_tree.tree.value)
		return ret_list
	}

	for len(node_cue) != 0 {
		current_node = node_cue[0]
		node_cue = node_cue[1:]

		if current_node.flag {
			ret_list = append(ret_list, current_node.value)
		} else {
			if current_node.smaller != nil && !current_node.smaller.flag {
				node_cue = append(node_cue, current_node.smaller)
			}

			current_node.flag = true
			node_cue = append(node_cue, current_node)

			if current_node.bigger != nil && !current_node.bigger.flag {
				node_cue = append(node_cue, current_node.bigger)
			}

			if current_node.parent != nil {
				node_cue = append(node_cue, current_node.parent)
			}
		}
	}

	return ret_list
}

func insert(main_tree binSubtree, value int) {
	if main_tree.value < 0 {
		main_tree.value = value
		main_tree.mini = &main_tree.value
		main_tree.maxi = &main_tree.value
		return
	}
	if value >= main_tree.tree.value {
		var check_tree binSubtree = *main_tree.tree.bigger
	} else {
		var check_tree binSubtree = *main_tree.tree.smaller
	}

}
