import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[9];
		
		for (int i = 0; i < arr.length; i++) {
			int n = sc.nextInt();
			arr[i] = n;
		}
		
		int max = arr[0];
		int index = 0;
		for (int i = 0; i < arr.length; i++) {
			if(arr[i] >= max){
				max = arr[i];
				index = i;
			}
		}
		System.out.println(max+"\n"+(index+1));
		sc.close();
	}
}