public class Studente extends Persona implements Comparable<Studente>{
	static public int studentiCreati=0;
	
	private String corso;
	private int annoDiFrequenza;
	public Studente() {
		super();
		
	}
	public Studente(String nome, int età, String corso, int annoDiFrequenza) {
        super(nome, età);
        this.corso = corso;
        this.annoDiFrequenza = annoDiFrequenza;
        studentiCreati++;
    }
	public String getCorso() {
		return corso;
	}
	public void setCorso(String corso) {
		this.corso = corso;
	}
	public int getAnnoDiFrequenza() {
		return annoDiFrequenza;
	}
	public void setAnnoDiFrequenza(int annoDiFrequenza) {
		this.annoDiFrequenza = annoDiFrequenza;
	}
	
	
	public String toString() {
		return "\n" + "Studente [corso=" + corso + ", annoDiFrequenza=" + annoDiFrequenza + ", toString()=" + super.toString()
				+ "]";
	}
	
	public int compareTo(Studente o) {
		return getNome().compareTo(o.getNome());
		
	}
	
}
