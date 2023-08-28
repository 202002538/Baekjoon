import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int length = sc.nextInt();
		int num = sc.nextInt();
		
		ArrayList<Integer> list = new ArrayList<>();
		
		for(int i = 0; i < length; i++){
			int n = sc.nextInt();
			if(n < num)
				list.add(n);
		}
		
		for(int a: list)
			System.out.print(a+" ");
		sc.close();
	}
}