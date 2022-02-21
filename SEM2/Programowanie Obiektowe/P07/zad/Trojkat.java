package com.company; //PRACOWNIA 7

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class Trojkat extends Figura implements Serializable {
    int wysokosc;
    int podstawa;
    String barwa;

    Trojkat(int wysokosc, int podstawa, String barwa, int pole, int obwod, int ilosc_bokow){
        this.wysokosc = wysokosc;
        this.podstawa = podstawa;
        this.barwa = barwa;
        this.pole = pole;
        this.obwod = obwod;
        this.ilosc_bokow = ilosc_bokow;
    }

    // spr
    Trojkat(int pole, int obwod, int ilosc_bokow){
        super(pole, obwod, ilosc_bokow);
    }

    public int getWysokosc() {
        return wysokosc;
    }

    public int getPodstawa() {
        return podstawa;
    }

    public String getBarwa() {
        return barwa;
    }

    public void setWysokosc(int wysokosc){
        this.wysokosc = wysokosc;
    }

    public void setPodstawa(int podstawa){
        this.podstawa = podstawa;
    }

    public void setBarwa(String barwa){
        this.barwa = barwa;
    }

    private void writeObject(ObjectOutputStream stream) throws IOException {
        stream.writeInt(pole);
        stream.writeInt(obwod);
        stream.writeInt(ilosc_bokow);
        stream.writeInt(wysokosc);
        stream.writeInt(podstawa);
        stream.writeUTF(barwa);
    }

    private void readObject(ObjectInputStream stream) throws IOException, ClassNotFoundException {
        pole = stream.readInt();
        obwod = stream.readInt();
        ilosc_bokow = stream.readInt();
        wysokosc = stream.readInt();
        podstawa = stream.readInt();
        barwa = stream.readUTF();
    }
    public String toString(){
        String result = "<html>INFORMACJE O FIGURZE: <br/> Trójkąt" + "<html><br/><html/>" + "Pole: " + pole
                + "<html><br/><html/>" + "Obwód: " + obwod + "<html><br/><html/>" + "Ilość boków: " + ilosc_bokow
                + "<html><br/><html/>" + "Wysokość: " + wysokosc + "<html><br/><html/>" + "Podstawa: " + podstawa
                + "<html><br/><html/>" + "Barwa: " + barwa;
        return result;
    }
}
