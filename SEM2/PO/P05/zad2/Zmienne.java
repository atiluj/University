package com.company; //pracowania 5 zadanie 2

import java.util.HashMap;

public class Zmienne extends Wyrazenie{
    String nazwa;
    int wartosc;

    Zmienne(String n, HashMap<String, Integer> war) throws NoSuchFieldException {
        nazwa = n;
        if (war.containsKey(n)) //wsadzmy n i sprawdzamy czy HashMap zawiera n
            wartosc = war.get(n);
        else throw new NoSuchFieldException("Nie ma tej zmiennej w hashmapie");
    }

    public int oblicz(){
        return wartosc;
    }

    public String toString() {
        return "(" + nazwa + " = " + wartosc + ")";
    }
}
