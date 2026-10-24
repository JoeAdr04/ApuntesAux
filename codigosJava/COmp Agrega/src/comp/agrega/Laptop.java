/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package comp.agrega;

import java.util.ArrayList;

/**
 *
 * @author jaeger
 */
public class Laptop {
    private String modelo;
    private int cantApp;
    private ArrayList<Aplicacion> apps = new ArrayList<>();
    private Pantalla pantalla = new Pantalla();

    public Laptop(String modelo, int cantApp, String tipo, int ancho, int alto) {
        this.modelo = modelo;
        this.cantApp = cantApp;
        this.pantalla = new Pantalla(tipo, ancho, alto);
        //this.pantalla = p; esta mal
    }
    public void agregaApp(Aplicacion app){//metodo necesario para resolver el problema
        this.apps.add(app);
        this.cantApp++;
    }
    public int getCantApp(){
        return this.cantApp;
    }
    public String getModelo(){
        return this.modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public void setCantApp(int cantApp) {
        this.cantApp = cantApp;
    }

    public void setPantalla(Pantalla pantalla) {
        this.pantalla = pantalla;
    }

    @Override
    public String toString() {
        return "Laptop{" + "modelo=" + modelo + ", cantApp=" + cantApp + ", pantalla=" + pantalla + '}';
    }
    
    
}
