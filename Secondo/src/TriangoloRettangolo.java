
public class TriangoloRettangolo {
	//devo dichiarare attributi/variabili e metodi/funzioni
	private double l1;
	private double l2;
	private double i;
	private double area;
	private double perimetro;
	
	
	public double getL1() {
		return l1;
	}
	public void setL1(double l1) {
		this.l1 = l1;
		UpdateFunctionalRelations();
		
	}
	private void UpdateFunctionalRelations() {
		// TODO Auto-generated method stub
		i=Math.sqrt(l2*l2+l1*l1);
		area= l1* l2 / 2;
		perimetro = l1+l2+i;
		
	}
	public double getL2() {
		return l2;
	}
	public void setL2(double l2) {
		this.l2 = l2;
		UpdateFunctionalRelations();
	}
	public double getI() {
		return i;
	}
	public double getArea() {
		return area;
	}
	public double getPerimetro() {
		return perimetro;
	}
	public TriangoloRettangolo(double l1, double l2) {
		super();
		this.l1 = l1;
		this.l2 = l2;
		
		//qui devo generare tutti gli altri valori
		UpdateFunctionalRelations();
	}	
	
	//è sufficente la conoscenza dei due cateti
	//per potere generare 
}
