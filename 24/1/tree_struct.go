package main

import (
	"log"
	"strconv"
)

type binSubtree struct {
	value   int
	flag    bool
	parent  *binSubtree
	bigger  *binSubtree
	smaller *binSubtree
}

type binTree struct {
	mini *binSubtree
	maxi *binSubtree
	size int // number of nodes
	tree *binSubtree
}

func GetMin(main_tree binTree) int {
	return main_tree.mini.value
}
func GetMax(main_tree binTree) int {
	return main_tree.maxi.value
}

func flagReset(main_tree binTree) *binTree {
	var ALL_NODES []int = Tree2Array(main_tree)
	var new_main_tree *binTree = new(binTree)

	for _, el := range ALL_NODES {
		new_main_tree = insert(new_main_tree, el)
	}

	return new_main_tree

}

func Tree2Array(main_tree binTree) []int {
	// inserts nodes to a array in order (min to max)

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
		current_node = node_cue[len(node_cue)-1]
		node_cue = node_cue[:len(node_cue)-1]

		if !current_node.flag {

			if current_node.parent != nil && !current_node.parent.flag {
				node_cue = append(node_cue, current_node.parent)
			}

			if current_node.bigger != nil && !current_node.bigger.flag {
				node_cue = append(node_cue, current_node.bigger)
			}

			current_node.flag = true
			node_cue = append(node_cue, current_node)

			if current_node.smaller != nil && !current_node.smaller.flag {
				node_cue = append(node_cue, current_node.smaller)
			}

		} else {
			ret_list = append(ret_list, current_node.value)
		}
		log.Printf("node_cue: %v\n", parse2int(node_cue))
	}

	pstring := ""

	for _, i := range ret_list {
		pstring += strconv.Itoa(i) + ","
	}

	log.Printf("Sorted array: %v", pstring)

	return ret_list
}

func parse2int(nodes []*binSubtree) []int {
	var ret_arr []int
	var ta int
	for _, a := range nodes {
		if a.bigger != nil || a.smaller != nil {
			ta = -1 * a.value
		} else {
			ta = a.value
		}
		ret_arr = append(ret_arr, ta)
	}
	return ret_arr
}

func insert(main_tree *binTree, value int) *binTree {

	tree_value := binSubtree{
		value:   value,
		bigger:  nil,
		smaller: nil,
	}

	if main_tree.size == 0 {
		log.Printf("Tree is empty. Inits value %v.", value)
		main_tree.size++
		main_tree.tree = &tree_value
		main_tree.maxi = main_tree.tree
		main_tree.mini = main_tree.tree
		return main_tree
	}

	current_node := main_tree.tree

	if value >= main_tree.maxi.value {
		main_tree.size++
		log.Printf("Value %v is the biggest we have seen.", value)
		current_node = main_tree.maxi
		current_node.bigger = &tree_value
		main_tree.maxi = current_node.bigger
		return main_tree
	} else if value < main_tree.mini.value {
		main_tree.size++
		log.Printf("Value %v is the smallest we have seen.", value)
		current_node = main_tree.mini
		current_node.smaller = &tree_value
		main_tree.mini = current_node.smaller
		return main_tree
	}

	log.Printf("Assessing value %v:", value)

	for {
		if value >= current_node.value {
			log.Print("\tIT's bigger")
			if current_node.bigger != nil {
				current_node = current_node.bigger
			} else {
				log.Print("\t\tBut no subtrees. Made tree.")
				current_node.bigger = &tree_value
				break
			}
		} else {
			log.Print("\tIT's samller")
			if current_node.smaller != nil {
				current_node = current_node.smaller
			} else {
				log.Print("\t\tBut no subtrees. Made tree.")
				current_node.smaller = &tree_value
				break
			}
		}
	}
	main_tree.size++

	return main_tree
}
