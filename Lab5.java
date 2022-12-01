package ctojp;
import java.util.Scanner;
public class Lab5 {
	public static void main(String args[]) {
		Scanner sc =new Scanner(System.in);
		System.out.print("Enter p(a even number):");
		int p =sc.nextInt();
		System.out.print("Enter q:");
		int q =sc.nextInt();
		System.out.println("Enter q and r (two +ve numbers):");
		int r =sc.nextInt();
		int s =sc.nextInt();
		if(q>r && s>p &&(r+s>(p+q))) {
			System.out.println("Correct values");
		}
		else {
			System.out.println("Wrong values");
		}
	}
}
