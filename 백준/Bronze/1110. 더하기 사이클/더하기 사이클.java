import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int original_num = sc.nextInt();
		int num = original_num;
		int new_num = -1;
		int cycle = 0;
		
		while(new_num != original_num){
			new_num = (num / 10) + (num % 10);
			new_num = (num % 10)*10 + (new_num % 10);
			num = new_num;
			cycle++;
		}
		System.out.println(cycle);
		sc.close();
	}
}