package test;

public class Seminar {
	public static void main(String args[]) {
		int sp=45;
		byte b=37;
		short s=32767;
		long l=50953085895L;
		float f=32.37F;
		double d=45.43910D;
		char c='G';
		boolean B=(10>9);
		System.out.println("The type of sp is: "+((Object)sp).getClass().getSimpleName());
		System.out.println("The type of b is: "+((Object)b).getClass().getSimpleName());
		System.out.println("The type of s is: "+((Object)s).getClass().getSimpleName());
		System.out.println("The type of l is: "+((Object)l).getClass().getSimpleName());
		System.out.println("The type of f is: "+((Object)f).getClass().getSimpleName());
		System.out.println("The type of d is: "+((Object)d).getClass().getSimpleName());
		System.out.println("The type of c is: "+((Object)c).getClass().getSimpleName());
		System.out.println("The type of B is: "+((Object)B).getClass().getSimpleName());
		System.out.println(B);
	}
}
