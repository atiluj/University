package com.company;//Julita Osman 314323 pracowania 5 zadanie 2
import java.util.HashMap;

public class Main2 {

    public static void main(String[] args) throws NoSuchFieldException {

        HashMap<String, Integer> wartosc = new HashMap<>();
        wartosc.put("x", 1);
        wartosc.put("y", 4);

        //constructing ((10X) + 1)/ Y
        Wyrazenie e1 = new Zmienne("x", wartosc);
        Wyrazenie e2 = new Liczby(2);
        Wyrazenie e3 = new Operacje("-", e1, e2);
        Wyrazenie e4 = new Liczby(9);
        Wyrazenie e5 = new Operacje("+", e3, e4);
        Wyrazenie e6 = new Zmienne("y", wartosc);
        Wyrazenie e7 = new Operacje("/", e5, e6);

        System.out.println("Postac wyrazenia 1: ");
        System.out.println(e7);
        System.out.println("Wartosc wyrazenia: " + e7.oblicz());

        Wyrazenie e8 = new Zmienne("y", wartosc);
        Wyrazenie e9 = new Liczby(0);
        Wyrazenie e10 = new Operacje("*", e8, e9);

        System.out.println("Postac wyrazenia 2: ");
        System.out.println(e10);
        System.out.println("Wartosc wyrazenia: " + e10.oblicz());
    }
}