import org.apache.http.Header;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.khrapov.pegsolitaire.solver.Board;
import org.khrapov.pegsolitaire.solver.Move;
import org.khrapov.pegsolitaire.solver.Position;
import org.khrapov.pegsolitaire.solver.PruningSearch;

import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
public class Main {

	public static String FLAG = "";
	
	public static void main(String[] args) {
	
		System.out.println("Solving...");
		Puzzle puzzle = getPuzzle();
		
		boolean search = true;
		
		int level = 1;
		while (search) {
			
			Board b = new Board(puzzle.M , puzzle.N, puzzle.src_board, puzzle.dest_board);
			Position p = b.initialPosition(puzzle.initial_points);
			
			PruningSearch pruningSearch = new PruningSearch(p);
			pruningSearch.prune(15000);
			int solutions = pruningSearch.search();
//			System.out.printf("-> %d\n", level);

			if (solutions > 0) {
				List<Move> sol = pruningSearch.getSolution(0);
				JSONObject payload = createPayload(puzzle, sol);
				puzzle = solvePuzzle(payload);
				if (puzzle == null) {
					search = false;
					
				}
			}
			else {
				System.out.println("no solution for level " + level);
				System.out.println(puzzle.M + " X " + puzzle.N);
				System.out.println(puzzle.src_board);
				System.out.println(puzzle.dest_board);
				System.out.println(puzzle.initial_points);
				search = false;
			}
			
			level++;
			
		}
		System.out.println(FLAG);


		
		
	}
	
	
	public static JSONObject createPayload(Puzzle puzzle, List<Move> sol) {
		try {
		JSONObject json = new JSONObject();
		JSONArray solution = new JSONArray();
		for (Move m : sol) {
			JSONArray step = new JSONArray();
			step.put(m.y1);
			step.put(m.x1);
			step.put("" + m.dir);
			solution.put(step);
		}
			json.put("puzzle_id", puzzle.puzzle_id);
			json.put("solution", solution);
			return json;
		} 
		catch (JSONException e) {
			e.printStackTrace();
		}
		return null;
		
	}
	
	public static String printSol(List<Move> sol) {
		String res = "[";
		System.out.print("[");
		for (Move m : sol) {
			System.out.print(m);
			res += m.toString();
			if (sol.indexOf(m) != sol.size() -1) {
				res += ',';
				System.out.print(",");
			}
		}
		res += "]";
		System.out.print("]");
		return res;
	}
	
	public static class Puzzle {
		public String puzzle_id;
		private JSONArray source_board;
		private JSONArray destination_board;
		public String msg;
		private ArrayList<Integer> initialPoints;
		public int[] src_board;
		public int[] dest_board;
		public int[] initial_points;
		public int M;
		public int N;
		
		public Puzzle(String puzzle_id, JSONArray source_board, JSONArray destination_board, String msg) {
			this.puzzle_id = puzzle_id;
			this.source_board = source_board;
			this.destination_board = destination_board;
			this.msg = msg;
			if (msg != null) {
				System.out.println(msg);
				FLAG += msg.charAt(0);
			}
			this.initialPoints =  new ArrayList<Integer>();
			
			this.src_board = getBoardArray(this.source_board, true);
			this.dest_board = getBoardArray(this.destination_board, false);
			this.initial_points = convertIntegers(this.initialPoints);
		}
		
		private int[] getBoardArray(JSONArray board, boolean isSource) {
			try {
				ArrayList<Integer> x = new ArrayList<Integer>();
				ArrayList<String> rows = new ArrayList<String>();
				
				this.M = board.length();
				for (int i = 0; i < this.M; i++) {
						rows.add(board.getString(i));
				}
				
				this.N = rows.get(0).length();
				
				for (int i = 0; i < this.N; i++) {
					for (int j = 0; j < rows.size(); j++) {
						char ch = rows.get(j).charAt(i);
						if (ch == 'O') {
							x.add(1);
						}
						else if (ch == '.') {
							if (isSource) {
								x.add(1);
								this.initialPoints.add(j);
								this.initialPoints.add(i);
							} else {
								x.add(0);
							}
							
						} else {
							x.add(2);
						}
						
					}
				}
				
				return convertIntegers(x);
				
				
			} catch (JSONException e) {
				e.printStackTrace();
			}
			return null;
			
		}
		
		private static int[] convertIntegers(List<Integer> integers)
		{
		    int[] ret = new int[integers.size()];
		    Iterator<Integer> iterator = integers.iterator();
		    for (int i = 0; i < ret.length; i++)
		    {
		        ret[i] = iterator.next().intValue();
		    }
		    return ret;
		}
	}
	
	public static Puzzle getPuzzle() {
		
		try {
			HttpClient httpClient = HttpClientBuilder.create().build();
		    HttpGet request = new HttpGet("https://puzzword.csa-challenge.com/puzzle");
		    request.addHeader("content-type", "application/json");
		    HttpResponse response = httpClient.execute(request);
		    HttpEntity entity = response.getEntity();
		    String json = EntityUtils.toString(entity, StandardCharsets.UTF_8);
		    JSONObject o = new JSONObject(json);
		    String msg = o.getString("message");
		    JSONObject data = new JSONObject(msg);
		    // System.out.println(msg);
		    return new Puzzle(data.getString("puzzle_id"), data.getJSONArray("source_board"), data.getJSONArray("destination_board"), null);
		} catch (Exception ex) {
			System.out.println(ex.toString());
			return null;
		}
	}
	
	
	public static Puzzle solvePuzzle(JSONObject payload) {
		HttpClient httpClient = HttpClientBuilder.create().build();
		try {
		    HttpPost request = new HttpPost("https://puzzword.csa-challenge.com/solve");
		    StringEntity params = new StringEntity(payload.toString());
		    request.addHeader("content-type", "application/json");
		    request.setEntity(params);
		    HttpResponse response = httpClient.execute(request);
		    HttpEntity entity = response.getEntity();
		    String json = EntityUtils.toString(entity, StandardCharsets.UTF_8);
		    JSONObject o = new JSONObject(json);
		    String msg = o.getString("message");
		    JSONObject data = new JSONObject(msg);
		    // System.out.println(msg);
		    if (data.has("puzzle_id")) {
		    	return new Puzzle(data.getString("puzzle_id"), data.getJSONArray("source_board"), data.getJSONArray("destination_board"), data.getString("message"));		    	
		    }
//		    System.out.println(o);
		    String finalMsg = data.getString("message");
		    System.out.println(finalMsg);
		    FLAG += finalMsg.charAt(0);
		    return null;
		} catch (Exception ex) {
			System.out.println(ex.toString());
			return null;
		}
	}

}
