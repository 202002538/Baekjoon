import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Map<Integer, int[]> map = new HashMap<>();
		int n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			int arr[] = {sc.nextInt(), sc.nextInt()};
			map.put(i, arr);
		}
			
		for (int i = 0; i < map.size(); i++) {
			int rate = 1;
			for (int j = 0; j < map.size(); j++) {
				if(i != j){
					if((map.get(i))[0] < map.get(j)[0] && (map.get(i))[1] < map.get(j)[1]) rate++;
				}
			}
			System.out.print(rate+ " ");
		}
		sc.close();
	}
}