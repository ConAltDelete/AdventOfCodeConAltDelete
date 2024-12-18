package main

import (
	"reflect"
	"testing"
)

func Test_digitaliser_varehus(t *testing.T) {
	type args struct {
		varehus *Warehouse
	}
	tests := []struct {
		name string
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			digitaliser_varehus(tt.args.varehus)
		})
	}
}

func Test_moveFish_1D(t *testing.T) {
	type args struct {
		space       []int
		lanternfish int
		command     int
	}
	tests := []struct {
		name  string
		args  args
		want  []int
		want1 int
	}{
		{
			name: "Move in positive direction without Wall",
			args: args{
				space:       []int{WALL, AIR, AIR, AIR, AIR, AIR, WALL},
				lanternfish: 3,
				command:     +1,
			},
			want:  []int{WALL, AIR, AIR, AIR, AIR, AIR, WALL},
			want1: 4,
		},
		{
			name: "Move in positive direction with Wall",
			args: args{
				space:       []int{WALL, AIR, AIR, AIR, WALL, AIR, WALL},
				lanternfish: 3,
				command:     +1,
			},
			want:  []int{WALL, AIR, AIR, AIR, WALL, AIR, WALL},
			want1: 3,
		},
		{
			name: "Move in positive direction with Box",
			args: args{
				space:       []int{WALL, AIR, AIR, AIR, BOX, AIR, WALL},
				lanternfish: 3,
				command:     +1,
			},
			want:  []int{WALL, AIR, AIR, AIR, AIR, BOX, WALL},
			want1: 4,
		},
		{
			name: "Move in positive direction with 2 Boxes",
			args: args{
				space:       []int{WALL, AIR, AIR, BOX, BOX, AIR, WALL},
				lanternfish: 2,
				command:     +1,
			},
			want:  []int{WALL, AIR, AIR, AIR, BOX, BOX, WALL},
			want1: 3,
		},
		{
			name: "Move in positive direction with Box against Wall",
			args: args{
				space:       []int{WALL, AIR, AIR, AIR, BOX, WALL, WALL},
				lanternfish: 3,
				command:     +1,
			},
			want:  []int{WALL, AIR, AIR, AIR, BOX, WALL, WALL},
			want1: 3,
		},
		{
			name: "Move in negative direction",
			args: args{
				space:       []int{WALL, AIR, AIR, AIR, BOX, WALL, WALL},
				lanternfish: 3,
				command:     -1,
			},
			want:  []int{WALL, AIR, AIR, AIR, BOX, WALL, WALL},
			want1: 2,
		},
		{
			name: "Move in negative direction against 2 boxes",
			args: args{
				space:       []int{WALL, AIR, BOX, BOX, AIR, WALL, WALL},
				lanternfish: 4,
				command:     -1,
			},
			want:  []int{WALL, BOX, BOX, AIR, AIR, WALL, WALL},
			want1: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := moveFish_1D(tt.args.space, tt.args.lanternfish, tt.args.command)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("moveFish_1D() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("moveFish_1D() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func Test_map_line(t *testing.T) {
	type args struct {
		y_coord int
		line    string
	}
	tests := []struct {
		name  string
		args  args
		want  []int
		want1 *Fish
	}{
		{
			name: "THE WALL LINE",
			args: args{
				y_coord: 0,
				line:    "##########",
			},
			want:  []int{WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL},
			want1: nil,
		},
		{
			name: "An 'empty' line (filled with AIR stopped by walls)",
			args: args{
				y_coord: 0,
				line:    "#........#",
			},
			want:  []int{WALL, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, WALL},
			want1: nil,
		},
		{
			name: "A line with BOXes",
			args: args{
				y_coord: 0,
				line:    "#...O.O..#",
			},
			want:  []int{WALL, AIR, AIR, AIR, BOX, AIR, BOX, AIR, AIR, WALL},
			want1: nil,
		},
		{
			name: "A line with Fish",
			args: args{
				y_coord: 0,
				line:    "#...O@O..#",
			},
			want:  []int{WALL, AIR, AIR, AIR, BOX, AIR, BOX, AIR, AIR, WALL},
			want1: &Fish{pos: [2]int{5, 0}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := map_line(tt.args.y_coord, tt.args.line)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("map_line() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("map_line() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}
