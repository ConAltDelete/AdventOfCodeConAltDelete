package main

import (
	"testing"
)

func TestListInit(t *testing.T) {
	list := new(circ_list)

	if list.index != 0 || list.value != 0 || list.next != nil || list.pre != nil {
		t.Log("Skule få {0,0,nil,nil}, men fikk {",list.index,",",list.value,",",list.next,",",list.pre)
		t.Fail()
	}
}
