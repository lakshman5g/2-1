package test;

public class Fibonacci {
	public static void main(String args[]) {
		int a,b,c;
		a=-1;
		b=1;
		for(int n=7;n!=0;n--) {
			c=a+b;
			System.out.println(c);
			a=b;
			b=c;
		}
	}
}
