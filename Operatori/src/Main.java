
public class Main {

	public static void main(String[] args) {
		{
			for (int i= 0;i <100;i++) {
				System.out.println(i);
			}
		}
		{
			int i = 0;
			while(i<100) {
				System.out.println(i);
				i= i+1;
			}
		}
		{
			int i = 0;
			do {
				System.out.println(i);
				i = i+1;
			} while (i<100);
		}
		{
			String i="Embè";
			switch (i) {
			case "Cosa" : {//istruzioni...
				System.out.println("Cosa");
			}
				break;
			case "Va bene": {// istruzioni...
				System.out.println("Va bene");
			}
				break;
			default:
				//istruzioni che saranno eseguite se nessun case è verificato
				System.out.println("Default");
				break; 
				
			case "Embè":{ //istruzioni...
				System.out.println("Embè");
			}
				break;
				//altri case...
			}
		}
		
		
	}

}
