public class Esercizio1 {

    public static void main(String[] args) {
       
        computer pc1 = new computer(1000, 2.5, 35, 25, 3, "Dell", 2022);
        computer pc2 = new computer(1500, 2.0, 32, 22, 2.5, "HP", 2023);

       
        System.out.println("Dettagli del primo computer:");
        pc1.stampaDettagliComputer();
        
        System.out.println("\nDettagli del secondo computer:");
        pc2.stampaDettagliComputer();

        
        computer.stampaNumeroComputerCreati();
    }
}
