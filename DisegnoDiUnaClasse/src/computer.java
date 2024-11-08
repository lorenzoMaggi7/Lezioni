public class computer {
    
    private double prezzo;
    private double peso;
    private double larghezza;
    private double altezza;
    private double profondita;
    private String produttore;
    private int annoProduzione;

    
    private static int numeroComputerCreati = 0;

    
    public computer(double prezzo, double peso, double larghezza, double altezza, double profondita, String produttore, int annoProduzione) {
        this.prezzo = prezzo;
        this.peso = peso;
        this.larghezza = larghezza;
        this.altezza = altezza;
        this.profondita = profondita;
        this.produttore = produttore;
        this.annoProduzione = annoProduzione;
        numeroComputerCreati++;  
    }

    
    public double getPrezzo() {
        return prezzo;
    }

    public void setPrezzo(double prezzo) {
        this.prezzo = prezzo;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getLarghezza() {
        return larghezza;
    }

    public void setLarghezza(double larghezza) {
        this.larghezza = larghezza;
    }

    public double getAltezza() {
        return altezza;
    }

    public void setAltezza(double altezza) {
        this.altezza = altezza;
    }

    public double getProfondita() {
        return profondita;
    }

    public void setProfondita(double profondita) {
        this.profondita = profondita;
    }

    public String getProduttore() {
        return produttore;
    }

    public void setProduttore(String produttore) {
        this.produttore = produttore;
    }

    public int getAnnoProduzione() {
        return annoProduzione;
    }

    public void setAnnoProduzione(int annoProduzione) {
        this.annoProduzione = annoProduzione;
    }

    
    public static void stampaNumeroComputerCreati() {
        System.out.println("Numero di computer creati: " + numeroComputerCreati);
    }

    
    public void stampaDettagliComputer() {
        System.out.println("Produttore: " + produttore);
        System.out.println("Anno di Produzione: " + annoProduzione);
        System.out.println("Prezzo: " + prezzo);
        System.out.println("Peso: " + peso);
        System.out.println("Dimensioni (LxAxP): " + larghezza + "x" + altezza + "x" + profondita);
    }
}
