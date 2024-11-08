
public class P20241021 {

	public static void main(String[] args) {
		
		for (int i = 0; i<10; i++) {
			System.out.println(i);
		}
		
		//for (;;) {
		//	System.out.println("Ciao");
		//}
		
		int i1 = 20;
		for(; i1<25; i1+=10) {
			System.out.println(i1);
		}
		
		
		for (int i=0;i<10;i++) {
			double d = Math.random();
			System.out.println(d);
		}
		
		for (int i=0;i<10;i++) {
			double d = Math.random();
			System.out.println(((i<9)?" ":"")+ (i + 1) + ")" + d);
		}
		//operatore ternario, 
		//<espressionelogica>?<valore se true>:<valore se false>
		
		for (int i=0;i<10;i++) {
			double d = Math.random();
			System.out.printf("%2d\t%4.3g\n" , i + 1, d);
		
	}
		/*
		 * System.out.printf è un metodo che vuolevcome parametri
		 * 1) una stringa di formato
		 * 2) un elenco di variabili i cui valori
		 *    saranno inseriti nella stringa risultante
		 *    in corrispondenza dei caratteri %<dgcs..> dove
		 *    d: intero
		 *    c: char
		 *    g: float
		 *    s: string
		 *    ...
		 *    Inoltre nella stringa di formato
		 *    \n => vai a capo a nuova riga
		 *    \r => vai a capo sulla riga corrente
		 *    \t => inserisci un tab
		 *    Tutto quello che non è %<...> oppure \.
		 *    viene riportato in stampa così com'è 
		 */
		
		int ni = 10;
		System.out.printf("Il numero è : %d\n", ni);
		
		int ne = 44;
		System.out.printf("Il numero è : %d, %d\n", ne);
		
		
		System.out.printf("Il numero è : (%d,%d)\n", ni, ne);
		
		/*
		 * Subito dopo il % e prima dei modificatori (d, f, g, s, b, ...)
		 * è possibile mettere un valore intero che indica la dimensione
		 * del campo
		 * se il valore è decimale allora posso scrivere
		 * <dimensioni totali>.<dimensioni dopo la virgola>
		 * esempio %7.3g => in totale 7 digit di cui 3 dopo la virgola
		 */
		
		System.out.printf("Numero libero: %07d\n", 987);
		System.out.printf("Numero libero: %07d\n", 1123987);
		
	

		//tra 0 e 2000
		double d=Math.random()*2000;
		
		//tra 1000 e 2000
		d=Math.random()*(2000-1000)+1000;

		//Tra a e b
		double a=1000;
		double b=1987;
		d=Math.random()*(b-a)+a;
		
		//e una stringa casuale?
		String alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
		int pos = (int)(Math.random()%alfabeto.length());
		
		String result="";
		result += alfabeto.charAt(pos);
	}
	
	
	
	
	
	
}

