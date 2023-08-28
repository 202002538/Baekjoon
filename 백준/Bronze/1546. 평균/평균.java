import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		double max = 0;
		double sum = 0;
		
		double[] arr = new double[num];
		for (int i = 0; i < num; i++) {
			double score = sc.nextInt();
			arr[i] = score;
			if (score > max) 
				max = score;
		}

		for (int i = 0; i < num; i++) {
			arr[i] = arr[i] / max * 100;
			sum += arr[i];
		}
		
		System.out.println(sum / num);
		sc.close();
	}
}