package Aula04;

public class Construtor {
    public static void main(String[] args) {
        Caneta c2 = new Caneta("BIC_Action", "Amarelo", 0.4f);
        c2.status();
        
        Caneta c3 = new Caneta("Compactor", "Preta", 0.75f);
        c3.status();
    }
}
