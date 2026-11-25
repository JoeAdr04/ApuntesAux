/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.test03;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author erenb
 */
public class ArchEstudiante {
    private String ruta;
    private Gson gson;

    public ArchEstudiante(String ruta) {
        this.ruta = ruta;
        this.gson = new GsonBuilder().setPrettyPrinting().create();
        
        File archivo = new File(this.ruta);
        if(!archivo.exists()){
            try(FileWriter writer = new FileWriter(archivo)){
                gson.toJson(new ArrayList<Estudiante>(), writer);
            }
            catch(IOException e){
                System.out.println("Error al crear el archivoi"+ e.getMessage());
            }
        }
    }
    
    public List<Estudiante> leer() {
        List<Estudiante> datos = new ArrayList<>();
        try (FileReader reader = new FileReader(this.ruta)) {
            // Definimos el tipo exacto de la lista para que Gson sepa en qué convertir el JSON
            Type tipoLista = new TypeToken<ArrayList<Estudiante>>() {}.getType();
            datos = gson.fromJson(reader, tipoLista);
            
            // Si el archivo estaba vacío, fromJson devuelve null
            if (datos == null) {
                datos = new ArrayList<>();
            }
        } catch (Exception e) {
            System.out.println("Ha fallado todo lo que podía fallar al leer: " + e.getMessage());
            datos = new ArrayList<>();
        }
        return datos;
    }
    
    public void modificar(List<Estudiante> listaEstudiantes) {
        try (FileWriter writer = new FileWriter(this.ruta)) {
            gson.toJson(listaEstudiantes, writer);
        } catch (Exception e) {
            System.out.println("Ha fallado todo lo que podía fallar al modificar: " + e.getMessage());
        }
    }
    
    
    
}
