
public class Secondo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Prima riga");
		System.out.println("Seconda riga");
		System.out.println("Terza riga");
		
		byte b1 = 10;
		byte b2;
		b2 = 100;
		byte b3, b4, b5;
		
		System.out.println("Il valore di b1 è : " + b1);
		b1 = 127;
		System.out.println("Il valore di b1 è " + b1);
		b1 += 1;
		System.out.println("Il valore di b1 è: " + b1);
		
		
		double d1=2.3;
		float f1= 2.3F;
		
		
		/*Operatori aritmetici
		 * +
		 * -
		 * *
		 * "/"
		 * %
		 * && (and)
		 * || (or)
		 * 
		 * Logica binaria
		 * & (and)
		 * | (or)
		 */
		
		
		/*Esercizio: definite la due variabili v1 e v2 di tipo intero, 
		 * assegnate a v1 il valore 35 e v2 il valore 41, 
		 * stampate l'and logico tra v1 e v2, 
		 * stampate l'and binario tra v1 e v2, 
		 * discutete i risultati
		 */
		int v1 = 35;
		int v2 = 41;
		
		
		System.out.println(v1 & v2);
		
		/* altri operatori aritmetici
		 * ++
		 * --
		 * +=
		 * *=
		 *"/="
		 * &=
		 * |=
		 * ^=
		 * CONFRONTO
		 * <
		 * >
		 * ==
		 * <=
		 * >=
		 * poi gli operatori di shifting
		 * <<
		 * >>
		 * >>=
		 * <<=
		 * ecc...
		 */
		
		float lato1 = 45.3f;
		float lato2 = 67.2f;
		
		
		float area = (lato1 * lato2) / 2;
		System.out.println(area);
		
		double ipotenusa = Math.sqrt(lato1 * lato1) + (lato2 * lato2);
		System.out.println(ipotenusa);
		
		
	}

}
