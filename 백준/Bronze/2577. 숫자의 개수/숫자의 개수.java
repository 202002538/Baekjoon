import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		int r = a * b * c;
		String[] arr = Integer.toString(r).split("");
		
		for (int i = 0; i < 10; i++) {
			int count = 0;
			for (int j = 0; j < arr.length; j++) {
				if(Integer.parseInt(arr[j]) == i)
					count++;
			}
			System.out.println(count);
		}
		sc.close();
		
	}
}