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
    
    public void mostrar(){
        for(int i=0; i<(this.jugadores).size(); i++){
            System.out.println("jugador: "+this.jugadores.get(i)+ " diamantes: "+ this.diamantes.get(i));
        }
    }
    
}
