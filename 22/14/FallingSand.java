import java.io.FileReader;
import java.io.BufferedReader;
import java.util.Vector;
import java.util.Set;
import java.util.Stack;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.lang.Integer;

/*
 *	Falling sand simulation for "Advent of code" 2022 day 14
 *	@see https://adventofcode.com/2022/day/14
 *	
 * */
public class FallingSand {
	
	public class Wall {
		/*
		 *	Wall objec to check if particle hits or not. Can also absorb particle to extend its parameter.
		 * */
		
		Integer[] Start;
		Integer[] Fin;

		public Wall(Integer[] Start, Integer[] Fin) {
			this.Start = Start;
			this.Fin = Fin;
		}

		/*
		 * 	Takes the start-end pair of coordianes and generates the points inbetween in a Taxicab-grid (Minkowski p=1).
		 *  If the coordinates are different in both axis, it will form two lines and follow Taxicab geometri with the fewes segments (2 lines).
		 * 
		*/
		public Vector<ArrayList<Integer>> Get_points() throws Exception {
			if(this.Start == null && this.Fin == null){ // Values not set
				throw new Exception("Start and end values are not set.");
			}
			
			// Check if one component is static, then automatic iterate the other.

			Vector<ArrayList<Integer>> ret = new Vector<>();

			ArrayList<Integer> intermediate_coord;
			for (int X_start = this.Start[0]+1; X_start < this.Fin[0]; X_start++){ // if different then itr runs, otherwise it does not. Same for the other loop.
				intermediate_coord = new ArrayList<>( Arrays.asList( new Integer[]{X_start,this.Fin[1]} ) );
				ret.add(intermediate_coord);
			}
			for (int Y_start = this.Start[1]+1; Y_start < this.Fin[1]; Y_start++){
				intermediate_coord = new ArrayList<>( Arrays.asList( new Integer[]{this.Fin[0],Y_start} ) );
				ret.add(intermediate_coord);
			}
			//System.out.println(ret.size());
			return ret;
		}

	}
	/*
	 *	Sand particle to fall through the maze that is the input.
	 *
	 *	@param X X-coordinate
	 *	@param Y Y-coordinate
	 *
	 * */
	public class Sand {

		Integer x; // X-coordinate
		Integer y; // Y-coordinate
		Integer[] Start;
		public Sand(int X, int Y) {
			this.x = X;
			this.y = Y;
			this.Start = new Integer[]{X,Y};
			path_stack.add(new ArrayList<>(Arrays.asList(new Integer[]{X,Y})));
		}

		/*
		 *	Changes the coordinates until particle falls to rest. If it falls to rest it becomes a wall.
		 * */
		public boolean Fall() {
			int[][] offset = {{0,1},{-1,1},{1,1}};
			ArrayList<Integer> new_coord;
			boolean wall_collition;
			for(int i = 0; i < offset.length; i++){
				System.out.print(i);
				new_coord = new ArrayList<>(Arrays.asList(new Integer[]{this.x + offset[i][0], this.y + offset[i][1]}));
				wall_collition = wall_set.contains(new_coord); //! Something wrong with the comperation. MIght be fixed after type correction.
				if(!wall_collition){
					this.x = new_coord.get(0);
					this.y = new_coord.get(1);
					if(i > 0){
						path_stack.add(new_coord);
					}
					return true;					
				}
			}
			ArrayList<Integer> new_wall = new ArrayList<>(Arrays.asList(new Integer[]{this.x,this.y}));
			wall_set.add(new_wall);
			return false;
		}

		/*
		 * Simulates the fall of a grain of sand by keeping track of last known position and applying "sand rules" to the objekt.
		*/
		public int Simulation(){
			ArrayList<Integer> last_path;
			int count = 0;
			int runtime_k = 0;
			System.out.println(Integer.toString(this.x) + "," + Integer.toString(this.y));
			while(this.y < 200 & runtime_k < 10000){ // runtime_k to prevent an infinit loop. 
				if(!this.Fall()){
					if(path_stack.isEmpty()){
						path_stack.add(new ArrayList<>(Arrays.asList(this.Start)));
					}
					last_path = path_stack.pop();
					this.x = last_path.get(0); // jumps back to last known working path since all sand has to take the same path.
					this.y = last_path.get(1);
					count++;
				}
				runtime_k++;
			}
			
			System.out.println("runtime: " + Integer.toString(runtime_k) + " count: " + Integer.toString(count) + " x,y: " + Integer.toString(this.x) +","+Integer.toString(this.y));
			System.out.println(path_stack.toString());
			// System.out.println(wall_set.toString());
			return count;
		}
	}

	/*
	 *	Reads input file and simpulates the falling sand.
	 * */
	public static void main(String[] args) {
		if(args.length > 0){
			read_file(args[0]);
		} else {
			read_file("./input");
		}

		//System.out.println("Size of cave: " + Integer.toString(wall_set.size()));

		FallingSand fallingSandInstance = new FallingSand(); // Create an instance of the outer class

		Sand particel = fallingSandInstance.new Sand(500, 0);

		System.out.println("Solution to part 1: " + Integer.toString(particel.Simulation()));
	}
	
	/*
	 *	Reads file for coordiantes to compute falling sand simulation.
	 *	
	 *	@param filename name of the file to be read. Must be a text file.
	 *	@return null
	 * */
	public static void read_file(String filename) { //! Need to correct insertion of new wall points.
		// read file
		//

		Vector<ArrayList<Integer>> collection_walls = new Vector<ArrayList<Integer>>();
		try (BufferedReader input_file = new BufferedReader(new FileReader(filename))){
			String line;
			ArrayList<Wall> walls;
			Vector<ArrayList<Integer>> inbetween_points;
			while ((line = input_file.readLine()) != null){ // iterating over file to convert to maze
				walls = parse(line);
				for(Wall obj: walls){
					inbetween_points = obj.Get_points();
					collection_walls.addAll(inbetween_points);
				}
			}
		} catch (Exception x) {
			System.err.format("Exception: %s%n", x);
		}
		if (wall_set == null){
			wall_set = new HashSet<>(collection_walls);
		} else {
			wall_set.addAll(collection_walls);
		}
		//for(int[] c: wall_set){
		//	System.out.print(Integer.toString(c[0]) + "," + Integer.toString(c[1]) + " ");
		//}
	}

	/*
	 *	Parses text of form "x1,y1 -> x2,y2 -> x3,y3 -> etc" into a collection of walls.
	 * */
	private static ArrayList<Wall> parse(String line) {
		String[] coords_array = line.trim().split(" -> ");
		Integer[] pre_coord;
		String[] coord_str = coords_array[0].trim().split(",");
		pre_coord = new Integer[]{Integer.parseInt(coord_str[0]),Integer.parseInt(coord_str[1])};
		
		Integer[] coord;
		FallingSand fallingSandInstance = new FallingSand();
		Wall temp_wall;
		ArrayList<Wall> collect_wall = new ArrayList<>();
		for(int i = 1; i < coords_array.length; i++){
			String[] coord1 = coords_array[i].trim().split(",");
			coord  = new Integer[]{Integer.parseInt(coord1[0]),Integer.parseInt(coord1[1])};
			temp_wall = fallingSandInstance.new Wall(pre_coord,coord);
			collect_wall.add(temp_wall);
			pre_coord = coord;
		}
		return collect_wall;
	}

	static Set<ArrayList<Integer>> wall_set;
	static Stack<ArrayList<Integer>> path_stack = new Stack<>();
}

