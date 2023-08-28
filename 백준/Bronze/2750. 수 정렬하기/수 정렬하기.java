import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int num = Integer.parseInt(br.readLine());
		int[] arr = new int[num];
		for (int i = 0; i < num; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		insertion_sort(arr);
		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}
	
	public static void insertion_sort(int[] A){
		for (int j = 1; j < A.length; j++) {
			int key = A[j];
			int i = j-1;

			while(i >= 0 && A[i] > key){
				A[i+1] = A[i];
				i--;
			}
			if(i + 1 != j) A[i+1] = key;
		}
	}
}