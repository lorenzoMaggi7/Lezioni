
public class Esercizio {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double l1 = 45.3;
		double l2 = 67.2;
		double i = Math.sqrt((l1 * l2) + (l2 * l2));
		
		double p = (l1 + l2 + i);
		double a = (l1 * l2) / 2;
		
		System.out.println("Ipotenusa: " + i);
		System.out.println("Perimetro: " + p);
		System.out.println("Area: " + a);
		
		
		
		double r = (i/4) * 3;
		double ac = (r * r) * 3.14;
		double pc = 2*(3.14 * r);
		
		System.out.println("Raggio: " + r);
		System.out.println("Perimetro: " + pc);
		System.out.println("Area cerchio: " + ac);
		
		
		System.out.println("Trigonometria");
		double x = Math.sin(45);
		System.out.println(x);
		double y = Math.sin(Math.PI/4);
		System.out.println(y);
		
		TriangoloRettangolo tr = new TriangoloRettangolo(3,4);
		
		System.out.println("Ipotenusa: " + tr.getI());
		System.out.println("Area: " + tr.getArea());
		
		tr.setL1(6);
		System.out.println("Ipotenusa: " + tr.getI());
		System.out.println("Area: " + tr.getArea());
		
		TriangoloRettangolo tr1 = new TriangoloRettangolo(900,0.2);
		tr1.setL2(9876);
		
		
	}

}




