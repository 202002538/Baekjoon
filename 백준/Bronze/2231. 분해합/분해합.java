import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		if(n <= 10 && n % 2 == 0) System.out.println(n / 2);
		else if (n <= 10 && n % 2 != 0) System.out.println(0);
		else{
			for (int i = 10; i <= n; i++) {
				int index = i;
				int sum = i;
				while(index != 0){
					sum += index % 10;
					index /= 10;
				}
				if(sum == n) {System.out.println(i); break;}
				else if(i == n-1) {System.out.println(0);}
			}
		}
		sc.close();
	}
}