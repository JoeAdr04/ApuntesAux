/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.test03;

import java.util.List;

/**
 *
 * @author erenb
 */
public class Test03 {

    public static void main(String[] args) {
        Estudiante e1 = new Estudiante("juan luis", 1234, 4567);
        ArchEstudiante a = new ArchEstudiante("estudiantes.json");

        // Leemos la lista de objetos Estudiante directamente
        List<Estudiante> arr = a.leer();
        
        // Agregamos el nuevo estudiante
        arr.add(e1);

        // Guardamos la lista actualizada
        a.modificar(arr);
    }
}
