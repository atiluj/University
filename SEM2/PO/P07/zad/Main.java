package com.company; //PRACOWNIA 7

import java.io.*;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<Figura> f1 = new ArrayList<>();
/*
        Figura t1 = new Trojkat(12, 3, "niebieski", 2, 3, 34);
        Figura t2 = new Trojkat(18, 6, "rozowy", 5, 13, 3);
        Figura t3 = new Okrag(12, 3, 0, 2, 3, "biel");
        Figura t4 = new Okrag(2, 2, 0, 2, 2, "czern");
        //Edytor e1 = new Edytor(f1);
        f1.add(t1);
        f1.add(t2);
        f1.add(t3);
        f1.add(t4);

        try{
            FileOutputStream fop = new FileOutputStream("figury.ser");
            ObjectOutputStream oop = new ObjectOutputStream(fop);
            oop.writeObject(f1);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }*/

        try{
            FileInputStream fis = new FileInputStream("figury.ser");
            ObjectInputStream ois = new ObjectInputStream(fis);
            ArrayList<Figura> lis = new ArrayList<>();
            lis = (ArrayList<Figura>) ois.readObject();
            InterfejsGraficzny int1 = new InterfejsGraficzny(lis);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        //InterfejsGraficzny i1 = new InterfejsGraficzny(f1);
        //Wyszukaj w1 = new Wyszukaj(f1);
        //Edytor2 ed1 = new Edytor2(f1);
    }
}
