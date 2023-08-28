import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		boolean go = true;
		
		while(go){
			int a = sc.nextInt();
			int b = sc.nextInt();
			if(a != 0 && b != 0)
				System.out.println(a+b);
			else
				go = false;
		}
		sc.close();
	}
}