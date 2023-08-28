import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int plus = 0;
		
		for (int i = 0; i < num; i++) {
			String str = sc.next();
			String[] arr = str.split("");
			int sum = 0;
			for (int j = 0; j < arr.length; j++) {
				if(arr[j].equals("O")){
					plus++;
					sum += plus;
				}else{
					plus = 0;
				}
			} System.out.println(sum); plus = 0;
		}sc.close();
	}
}