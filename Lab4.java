package ctojp;
import java.lang.Math;
import java.util.Scanner;
public class Lab4 {
	public static void main(String args[]) {
		Scanner s =new Scanner(System.in);
		System.out.println("Enter the first point:");
		double x1=s.nextInt();
		double y1=s.nextInt();
		System.out.println("Enter the second point:");
		double x2=s.nextInt();
		double y2=s.nextInt();			
		double a=(x2-x1)*(x2-x1)+(y2-y1)*(y2-y1);
		double dist=Math.sqrt(a);
		System.out.println("The distance between the given two points is :"+dist);
		}
	}

