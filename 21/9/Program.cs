using System;
using System.IO;
using System.Collections;

namespace _9 {
    class Program {
        static void Main(string[] args) {
            Console.Write("Part 1: ");
	    Program.part1();
            //Console.Write("Part 2: ");
	    //part2();
        }

	void part1(){
		String line;
		HashTable heatmap = new HashTable();
		StreamReader sr = new StreamReader(".\\heat");
		
		(int,int) coord;
		int row = 0;

		while(line != null){
			line = sr.ReadLine();
			for(int i = 0; i < line.Length; i++) {
				coord = (row,i);
				heatmap.add(coord,line[i]);
			}
		}
		sr.Close();

		HashSet<(int,int)> adi = new HashSet<(int,int)>();
		HashSet<(int,int)> remove_key = new HashSet<(int,int)>();
		HashSet<(int,int)> adi_next = new HashSet<(int,int)>();
		HashSet<(int,int)> minimum = new HashSet<(int,int)>();
		List<(int,int)> adi_n = new List<(int,int)>();

		while(adi.Length != 0){
			remove_key.Clear();
			adi_next.Clear();
			foreach((int,int) p in adi){
				adi_n = Program.gen_next(p,0,99,0,99);
				if (p == adi_n.MinBy(t => heatmap[t])){
					minimum.Add(p);
				} else {
					foreach((int,int) q in adi_n){
						if(heatmap[q] < heatmap[p]){
							adi.next.Add(q);
						}
					}
				}
				remove_key.Add(p);

			}
			adi = adi.UnionWith(adi_next).ExceptWith(remove_key);
		}
		int total = 0;

		foreach((int,int) p in minimum){
			total += heatmap[p] + 1;
		}
		Console.WriteLine(total);

	}
	List<(int,int)> gen_next((int,int) p, int x0, int x1, int y0, int y1){
		
	}
    }
}
