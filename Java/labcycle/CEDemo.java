package test;

public class CEDemo {
	public static void main (String args[])
	{
	try {
		int a,b,c,d;
		a=10;
		b=0;
		c=a/b;
		try {
			d=a/c;
		}catch(RunTimeException e) {
			System.out.println("Division with zero inside catch");
		}
	}catch(ArthimeticException e) {
		System.out.println ("Hai ");
	}
	} 
}
