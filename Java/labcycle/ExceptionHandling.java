package test;
import java.util.Scanner;
import java.util.InputMismatchException;
public class ExceptionHandling {
	public static void main(String args[]) {
		Scanner s = new Scanner(System.in);
		boolean continueloop=true;
		do {
			try {
				
				int num=s.nextInt();
				int den=s.nextInt();
				int r=num/den;
				continueloop=false;
			}
		catch(ArithmeticException e) {
			System.out.println("Exception raised :"+e);
			System.out.println("enter a non zero number to divide......Try again");
		}
		catch(InputMismatchException e) {
			System.out.println("Exception raised:"+e);
			s.nextLine();
			System.out.println(" u must enter integers only.PLs try again");
		}
		finally {
			System.out.println("Execution completed!!!!!!!!!!!");
		}
		}
		while(continueloop);

}
}
