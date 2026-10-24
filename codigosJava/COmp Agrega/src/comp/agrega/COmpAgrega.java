/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package comp.agrega;

import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author jaeger
 */
public class COmpAgrega {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Pantalla p = new Pantalla();
        
        //Laptop lap = new Laptop("samsung", 0, p); esta mal
        Laptop lap = new Laptop("samsung", 3, "lcd ips", 13, 7);
        Laptop lap1 = new Laptop("samsung", 12, "lcd ips", 13, 7);
        Laptop lap2 = new Laptop("samsung", 6, "lcd ips", 13, 7);
        Laptop lap3 = new Laptop("samsung", 24, "lcd ips", 13, 7);
        ArrayList<Laptop> vec = new ArrayList<>();
        vec.add(lap);
        vec.add(lap1);
        vec.add(lap2);
        vec.add(lap3);
        //inciso b
        int may =0;
        for (Laptop l: vec){
            if(l.getCantApp() > may){
                may = l.getCantApp();
            }
        }
        for (Laptop l: vec){
            if(l.getCantApp() == may){
                System.out.println(l);//mostramos el objeto completo, apra eso necesitamos toString()
            }
        }
        Scanner te = new Scanner(System.in);
        //inciso c
        String x;
        x = te.nextLine();
        for(Laptop laptop: vec){
            if(laptop.getModelo() == x){
                String nom;
                int tam;
                nom = te.nextLine();
                tam = te.nextInt();
                laptop.agregaApp(new Aplicacion(nom, tam));//recibe un objeto nuevo
            }
        }
    }
    
}
