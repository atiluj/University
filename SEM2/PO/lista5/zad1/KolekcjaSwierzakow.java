package com.company;
import java.util.ArrayList;

public class KolekcjaSwierzakow {
    ArrayList<Swierzaki> kolekcja;

    KolekcjaSwierzakow(){ //konstruktor pusta lista
        kolekcja = new ArrayList<Swierzaki>();
    }

    public void add(Swierzaki swierzak) {
        int rozmiar = kolekcja.size();

        if(rozmiar == 0) //gdy pusta
            kolekcja.add(swierzak);
        else if(swierzak.compareTo(kolekcja.get(0)) < 0) //gdy arakcyjnosc jest mniejszy od tego na pierwszym miejscu
            kolekcja.add(0, swierzak);
        else if(swierzak.compareTo(kolekcja.get(rozmiar-1)) > 0) //najwieksz atracyjnsc z nich wszystkich
            kolekcja.add(swierzak);
        else {
            int i;
            for(i = 0; i < rozmiar; i++) {
                if(swierzak.compareTo(kolekcja.get(i)) > 0 && swierzak.compareTo(kolekcja.get(i+1)) < 0)
                    break;
            }
            kolekcja.add(i, swierzak);
        }
    }

    @Override
    public String toString(){
        String result = "[";
        for(Swierzaki sw : kolekcja){
            result += sw.toString();
            result += ", \b";
        }
        result += "\b\b]";
        return result;
    }

    public Swierzaki pop(){
        Swierzaki result = kolekcja.remove(0);
        return result;

    }

}