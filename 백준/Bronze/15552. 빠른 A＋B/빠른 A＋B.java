import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int num = Integer.parseInt(br.readLine());
		
		for(int i = 1; i <= num; i++){
			String str = br.readLine();
			String[] a = str.split(" "); 
			bw.write((Integer.parseInt(a[0])+Integer.parseInt(a[1]))+"\n");
		}
		bw.flush();
	}
}