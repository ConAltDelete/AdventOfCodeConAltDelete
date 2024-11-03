package main

import (
	"reflect"
	"testing"
)

func Test_change_coord(t *testing.T) {
	type args struct {
		start  coord
		vector coord
	}
	tests := []struct {
		name  string
		args  args
		want  coord
		want1 coord
		want2 bool
	}{
		{
			name: "In-range movment.",
			args: args{
				start: coord{
					x: 10, y: 10, width: 20, hight: 20,
				},
				vector: coord{x: 2, y: 1, width: -1, hight: -1},
			},
			want:  coord{x: 12, y: 11, width: 20, hight: 20},
			want1: coord{x: 2, y: 1, width: -1, hight: -1},
			want2: false,
		}, {
			name: "Double edge reflection (positive).",
			args: args{
				start: coord{
					x: 9, y: 9, width: 10, hight: 10,
				},
				vector: coord{
					x: 2, y: 1, width: -1, hight: -1,
				},
			},
			want:  coord{x: 1, y: 8, width: 10, hight: 10},
			want1: coord{x: 2, y: -1, width: -1, hight: -1},
			want2: true,
		}, {
			name: "roof reflection (0-hight).",
			args: args{
				start: coord{
					x: 1, y: 1, width: 20, hight: 20,
				},
				vector: coord{
					x: 2, y: -2, width: -1, hight: -1,
				},
			},
			want:  coord{x: 3, y: 1, width: 20, hight: 20},
			want1: coord{x: 2, y: 2, width: -1, hight: -1},
			want2: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1, got2 := change_coord(tt.args.start, tt.args.vector)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("change_coord() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("change_coord() got1 = %v, want %v", got1, tt.want1)
			}
			if got2 != tt.want2 {
				t.Errorf("change_coord() got2 = %v, want %v", got2, tt.want2)
			}
		})
	}
}
