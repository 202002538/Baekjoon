import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		if (n == 0 || n == 1) System.out.println(n);
		else System.out.println(fibonacci(0, 1, n-1));
		sc.close();
	}
	
	public static int fibonacci(int a, int b, int n){
		if (n == 1) return a + b;
		else{
			int new_a = b;
			b = a + b;
			return fibonacci(new_a, b, n-1);
		}
	}
}