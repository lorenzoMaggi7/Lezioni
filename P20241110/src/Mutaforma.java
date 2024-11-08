
public class Mutaforma {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int a = somma(20,10);
		System.out.println(a);
		
		double b = somma(10.1,20.0);
		
		String s = somma("buona","giornata");
	}

	private static String somma(String string, String string2) {
		return string+string2;
	}

	private static double somma(double d, double e) {
		return d+e;
	}

	private static int somma(int i, int j) {
		return i+j;
	}

}
