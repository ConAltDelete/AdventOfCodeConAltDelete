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

			// System.out.println("Coords in -> Start: " + Arrays.toString(this.Start) + " End: " + Arrays.toString(this.Fin));

			ArrayList<Integer> conv_Start = new ArrayList<>(Arrays.asList(this.Start));
			ArrayList<Integer> conv_Fin = new ArrayList<>(Arrays.asList(this.Fin));

			return Compute_points(conv_Start,conv_Fin);
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
		Stack<ArrayList<Integer>> path_stack = new Stack<>();
		public Sand(int X, int Y) {
			this.x = X;
			this.y = Y;
			this.Start = new Integer[]{X,Y};
			//path_stack.push(new ArrayList<>(Arrays.asList(new Integer[]{X,Y})));
		}

		/**
		 *	Changes the coordinates until particle falls to rest. If it falls to rest it becomes a wall.
		 * 
		 * @return
		 */
		public boolean Fall() {
			int[][] offset = {{0,1},{-1,1},{1,1}};
			ArrayList<Integer> new_coord;
			boolean wall_collition;
			for(int i = 0; i < offset.length; i++){
				System.out.print(i);
				new_coord = new ArrayList<>(Arrays.asList(new Integer[]{this.x + offset[i][0], this.y + offset[i][1]}));
				wall_collition = wall_set.contains(new_coord);
				if(!sand_set.isEmpty()){
					wall_collition = wall_collition | sand_set.contains(new_coord);
				}
				if(!wall_collition){
					if(i > 0){
						path_stack.push(new ArrayList<>(Arrays.asList(new Integer[]{this.x,this.y})));
					}
					this.x = new_coord.get(0);
					this.y = new_coord.get(1);
					return true;					
				}
			}
			ArrayList<Integer> new_sandwall = new ArrayList<>(Arrays.asList(new Integer[]{this.x,this.y}));
			sand_set.add(new_sandwall);
			if(new_sandwall.get(0) > max_X){
				max_X = new_sandwall.get(0);
			}
			if(new_sandwall.get(0) < min_X){
				min_X = new_sandwall.get(0);
			}
			if(new_sandwall.get(1) > max_Y){
				max_Y = new_sandwall.get(1);
			}
			if(new_sandwall.get(1) < min_Y){
				min_Y = new_sandwall.get(1);
			}
			return false;
		}

		/**
		 * Simulates the fall of a grain of sand by keeping track of last known position and applying "sand rules" to the objekt.

		 * @return
		 */
		public int Simulation(){
			ArrayList<Integer> last_path;
			int count = 0;
			int runtime_k = 0;
			System.out.println(Integer.toString(this.x) + "," + Integer.toString(this.y));
			while(this.y < max_Y & runtime_k < 10000){ // runtime_k to prevent an infinit loop. 
				if(!this.Fall()){
					if(path_stack.isEmpty()){
						path_stack.push(new ArrayList<>(Arrays.asList(this.Start))); // return to known position (start position)
					}
					if(Arrays.equals(this.Start, new Integer[]{this.x,this.y})){
						break;
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
	
	enum elementType {AIR, ROCK, SAND, START, TRACE}
	static Integer max_X = -1000;
	static Integer max_Y = -1000;
	static Integer min_X = 1000;
	static Integer min_Y = 0;

	static Set<ArrayList<Integer>> wall_set = new HashSet<>();
	static Set<ArrayList<Integer>> sand_set = new HashSet<>();

	/**
	 *	Reads input file and simpulates the falling sand.
	 * */
	public static void main(String[] args) {
		if(args.length > 0){
			read_file(args[0]);
		} else {
			read_file("./input");
		}

		System.out.println("Size of cave: " + wall_set.toString());

		FallingSand fallingSandInstance = new FallingSand(); // Create an instance of the outer class

		Sand particel = fallingSandInstance.new Sand(500, 0);
		// System.out.println("Solution to part 1: " + Integer.toString(particel.Simulation()));

		max_Y = max_Y + 2; // part 2 info
		// Artifisaly add walls. Assume we have updated the max_Y.

		for(int x_left = min_X; x_left <= max_X; x_left++){
			wall_set.add(new ArrayList<>(Arrays.asList(new Integer[]{x_left,max_Y})));
		}

		System.out.println("Solution to part 2: " + Integer.toString(particel.Simulation()));

		try {
			viszuliseCave(particel);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}


	/**
	 *	Reads file for coordiantes to compute falling sand simulation.
	 *	
	 *	@param filename name of the file to be read. Must be a text file.
	 *	@return null
	 * */
	public static void read_file(String filename) {
		// read file
		//

		Vector<ArrayList<Integer>> collection_walls = new Vector<ArrayList<Integer>>();
		int count = 0;
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
				count++;
			}
		} catch (Exception x) {
			System.err.format("Exception: %s%n", x);
		}
		System.out.println("number of lines:" + Integer.toString(count));
		if (wall_set == null){
			wall_set = new HashSet<>(collection_walls);
		} else {
			wall_set.addAll(collection_walls);
		}
		//for(int[] c: wall_set){
		//	System.out.print(Integer.toString(c[0]) + "," + Integer.toString(c[1]) + " ");
		//}
	}
	static private Vector<ArrayList<Integer>> Compute_points(ArrayList<Integer> S, ArrayList<Integer> E) {
		Vector<ArrayList<Integer>> ret = new Vector<>();

		ArrayList<Integer> intermediate_coord;
		Integer minimum_X;
		Integer minimum_Y;
		Integer maximum_X;
		Integer maximum_Y;

		if (S.get(0) < E.get(0)){
			minimum_X = S.get(0);
			maximum_X = E.get(0);
		} else {
			minimum_X = E.get(0);
			maximum_X = S.get(0);
		}
		if (S.get(1) < E.get(1)){
			minimum_Y = S.get(1);
			maximum_Y = E.get(1);
		} else {
			minimum_Y = E.get(1);
			maximum_Y = S.get(1);
		}

		for (int X_start = minimum_X; X_start <= maximum_X; X_start++){
			intermediate_coord = new ArrayList<>( Arrays.asList( new Integer[]{X_start,maximum_Y} ) );
			ret.add(intermediate_coord);
		}
		for (int Y_start = minimum_Y; Y_start <= maximum_Y; Y_start++){
			intermediate_coord = new ArrayList<>( Arrays.asList( new Integer[]{maximum_X,Y_start} ) );
			ret.add(intermediate_coord);
		}
		// System.out.println(ret.toString());
		return ret;
	}

	/**
	 *	Parses text of form "x1,y1 -> x2,y2 -> x3,y3 -> etc" into a collection of walls.

	 * @param line
	 * @return
	 */
	private static ArrayList<Wall> parse(String line) {
		String[] coords_array = line.trim().split(" -> ");
		Integer[] pre_coord;
		String[] coord_str = coords_array[0].trim().split(",");
		pre_coord = new Integer[]{Integer.parseInt(coord_str[0]),Integer.parseInt(coord_str[1])};
		if(pre_coord[0] > max_X){
			max_X = pre_coord[0];
		}
		if(pre_coord[0] < min_X){
			min_X = pre_coord[0];
		}
		if(pre_coord[1] > max_Y){
			max_Y = pre_coord[1];
		}
		if(pre_coord[1] < min_Y){
			min_Y = pre_coord[1];
		}
		Integer[] coord;
		FallingSand fallingSandInstance = new FallingSand();
		Wall temp_wall;
		ArrayList<Wall> collect_wall = new ArrayList<>();
		for(int i = 1; i < coords_array.length; i++){
			String[] coord1 = coords_array[i].trim().split(",");
			coord  = new Integer[]{Integer.parseInt(coord1[0]),Integer.parseInt(coord1[1])};
			if(coord[0] > max_X){
				max_X = coord[0];
			}
			if(coord[0] < min_X){
				min_X = coord[0];
			}
			if(coord[1] > max_Y){
				max_Y = coord[1];
			}
			if(coord[1] < min_Y){
				min_Y = coord[1];
			}
			temp_wall = fallingSandInstance.new Wall(pre_coord,coord);
			collect_wall.add(temp_wall);
			pre_coord = coord;
		}
		return collect_wall;
	}
	/**
	 * 	Vizulises the cave that the sand need to thraverse.
	 * 
	 * @throws Exception
	 */
	private static void viszuliseCave(Sand particle) throws Exception {
		if(wall_set.isEmpty()){
			throw new Exception("There are no walls to vizulise.");
		}

		elementType[][] Cave = new elementType[max_Y - min_Y + 1][max_X - min_X + 1];

		System.out.println(new ArrayList<>(Arrays.asList(new Integer[]{min_X,max_X,min_Y,max_Y})));

		Integer curr_X;
		Integer curr_Y;

		for(int i = 0; i<Cave.length;i++){
			for(int j=0; j<Cave[i].length;j++){
				Cave[i][j] = elementType.AIR;
			}
		}
		Cave[particle.Start[1] - min_Y][particle.Start[0] - min_X] = elementType.START;

		for(ArrayList<Integer> W :wall_set){
			curr_X = W.get(0) - min_X;
			curr_Y = W.get(1) - min_Y;
			Cave[curr_Y][curr_X] = elementType.ROCK;
		}
		if(!sand_set.isEmpty()){
			for(ArrayList<Integer> W :sand_set){
				curr_X = W.get(0) - min_X;
				curr_Y = W.get(1) - min_Y;
				Cave[curr_Y][curr_X] = elementType.SAND;
			}
		}
		if(!particle.path_stack.isEmpty()){
			// particle.path_stack.push(new ArrayList<>(Arrays.asList(particle.Start)));
			ArrayList<Integer> pre_coord = particle.path_stack.get(0);
			Vector<ArrayList<Integer>> coll;
			for(int j = 1; j < particle.path_stack.size(); j++){
				coll = Compute_points(pre_coord, particle.path_stack.get(j));
				for(ArrayList<Integer> W :coll){
					curr_X = W.get(0) - min_X;
					curr_Y = W.get(1) - min_Y;
					Cave[curr_Y][curr_X] = elementType.TRACE;
				}
				pre_coord = particle.path_stack.get(j);
			}
		}

		System.out.print("\n");
		for(elementType[] row: Cave){
			for(elementType el: row){
				switch (el) {
					case elementType.ROCK:
						System.out.print("#");
						break;
					case elementType.SAND:
						System.out.print("O");
						break;
					case elementType.TRACE:
						System.out.print("~");
						break;
					case elementType.START:
						System.out.print("+");
						break;
					case elementType.AIR:
						System.out.print(".");
						break;
				
					default:
						break;
				}
			}
			System.out.print("\n");
		}
		System.out.print("\n");
	}
}

