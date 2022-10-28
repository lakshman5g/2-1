package test;

public class Test {
	public static void main(String args[]) {
		int a=45;
		boolean b=true;
		char c='s';
		String s="pranav";
		System.out.println(((Object)a).getClass().getSimpleName());
		System.out.println(((Object)b).getClass().getSimpleName());
		System.out.println(((Object)c).getClass().getSimpleName());
		System.out.println(s.getClass().getSimpleName());
	}
}
