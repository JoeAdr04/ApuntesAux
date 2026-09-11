package servidorminecraft;

import java.util.ArrayList;

public class Servidor {
    //private String[] jugadores =new String[10];
    private ArrayList<String> jugadores = new ArrayList();
    private ArrayList<Integer> diamantes = new ArrayList();

    public Servidor(String j1, int diamant) {
        this.jugadores.add(j1);
        this.diamantes.add(diamant);
    }
    
    public void agregarJugador(String jug, int diam){
        this.jugadores.add(jug);
        this.diamantes.add(diam);   
    }
   
    public void contarStacks(){
        int cont=0;
        for(int d: this.diamantes){
            System.out.println("jugador: "+this.jugadores.get(cont)+"tiene: "+d/64+" stacks de diamantes");
            cont++;
        }
    }
    public void nummayor () {
        int mayor = 0;
        for (int i = 0; i < this.diamantes.size(); i++) {
            if (this.diamantes.get(i) > mayor) {
                mayor = this.diamantes.get(i);
            }
        }
        for (int i = 0; i < this.diamantes.size(); i++) {
            if (this.diamantes.get(i) == mayor){
                System.out.println("JUgador con mas diamantes es: "+this.jugadores.get(i));
            }
        }
        
    }
    public int totaldiamantes() {
        int total = 0;
        for (int i = 0; i < this.diamantes.size(); i++) {
            total += this.diamantes.get(i);
        }
        return total;
    }
    public void mostrar(){
        for(int i=0; i<(this.jugadores).size(); i++){
            System.out.println("jugador: "+this.jugadores.get(i)+ " diamantes: "+ this.diamantes.get(i));
        }
    }
    
}
