import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] array = new int[n];
		for (int i = 0; i < array.length; i++) 
			array[i] = sc.nextInt();
		
		int maximum = 0;
		for (int i = 0; i < array.length; i++) {
			int a = array[i];
			for (int j = i+1; j < array.length; j++) {
				int b = array[j];
				if(a + b >= m) continue;
				else{
					for (int k = j+1; k < array.length; k++) {
						int c = array[k];
						if(a+b+c >= maximum && a+b+c <= m) maximum = a+b+c;
					}
				}
			}
			if(maximum == m) {break;}
		}
		System.out.println(maximum);
		sc.close();
	}
}