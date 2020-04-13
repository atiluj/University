package com.company;//Julita Osman 314323 pracowania 5 zadanie 2

public class Liczby extends Wyrazenie {
    int wartosc;

    public Liczby(int val){
        this.wartosc = val;
    }

    public int oblicz(){
        return wartosc;
    }

    public String toString(){
        String rezultat = "(Stała = " + wartosc + ")";
        return rezultat;
    }
}