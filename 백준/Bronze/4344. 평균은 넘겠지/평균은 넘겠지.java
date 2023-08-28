import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		for (int i = 0; i < num; i++) {
			int students = sc.nextInt();
			int sum = 0;
			int count = 0;
			int[] arr = new int[students];
			
			for (int j = 0; j < students; j++) {
				int score = sc.nextInt();
				sum += score;
				arr[j] = score;
			}
			double ave = sum / students;
			for(int a : arr){
				if(a > ave)
					count++;
			}
			double per = (double)count * 100 / (double)students;
			System.out.println(String.format("%.3f", per)+"%");
		}
	}
}
