package com.company;

public class Brokul implements Swierzaki{
    String imie;
    int atrakcyjnosc;
    int naklad;
    String uprawa = "krzak";

    boolean owoc = false;
    boolean warzyw = true;

    Brokul(String imie, int atrakcyjnosc, int naklad) //konstruktor
    {
        this.imie = imie;
        this.atrakcyjnosc = atrakcyjnosc;
        this.naklad = naklad;
    }

    @Override
    public int getAtrakcyjnosc() {
        return atrakcyjnosc;
    }

    public int getNaklad() {
        return naklad;
    }

    @Override
    public int compareTo(Swierzaki obj){
        int atrakcyjnosc2 = obj.getAtrakcyjnosc();
        if (atrakcyjnosc < atrakcyjnosc2) return -1;
        else if (atrakcyjnosc == atrakcyjnosc2) return 0;
        else return 1;
    }

    @Override
    public String toString(){
        String result;
        if(owoc == true)
        {
            result = "Brokul " + imie + " " + atrakcyjnosc + " owoc " +"\n";
        }
        else result = "Brokul " + imie + " " + atrakcyjnosc + " warzywo " + "\n";
        return result;
    }

}