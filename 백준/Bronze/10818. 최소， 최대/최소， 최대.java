import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[] arr = new int[num];
		
		for(int i = 0; i < num; i++){
			int n = sc.nextInt();
			arr[i] = n;
		}
		
		int min = arr[0];
		int max = arr[0];
		
		for (int i = 0; i < arr.length; i++) {
			if(arr[i] < min)
				min = arr[i];
			else if(arr[i] > max)
				max = arr[i];
		}
		
		System.out.println(min + " " + max);
		sc.close();
	}
}