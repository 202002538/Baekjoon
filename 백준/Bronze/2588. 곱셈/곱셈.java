import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		String b = sc.next();
		
		String[] num = b.split("");
		
		System.out.println(a * Integer.parseInt(num[2]));
		System.out.println(a * Integer.parseInt(num[1]));
		System.out.println(a * Integer.parseInt(num[0]));
		System.out.println(a * Integer.parseInt(b));
		sc.close();
	}
}