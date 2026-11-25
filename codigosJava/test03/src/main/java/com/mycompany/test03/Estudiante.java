/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.test03;

/**
 *
 * @author erenb
 */
public class Estudiante {
    private String nombre;
    private int carnet;
    private int matricula;

    public Estudiante(String nombre, int carnet, int matricula) {
        this.nombre = nombre;
        this.carnet = carnet;
        this.matricula = matricula;
    }

    public String getNombre() {
        return nombre;
    }

    public int getCarnet() {
        return carnet;
    }

    public int getMatricula() {
        return matricula;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setCarnet(int carnet) {
        this.carnet = carnet;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    @Override
    public String toString() {
        return "Estudiante{" + "nombre=" + nombre + ", carnet=" + carnet + ", matricula=" + matricula + '}';
    }
    
    
    
}
