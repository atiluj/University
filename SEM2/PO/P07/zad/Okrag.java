package com.company; //PRACOWNIA 7

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class Okrag extends Figura implements Serializable {
    int promien;
    int srednica;
    String kolor;

    Okrag(int pole, int obwod, int ilosc_bokow, int promien, int srednica, String kolor){
        this.promien = promien;
        this.srednica = srednica;
        this.kolor = kolor;
        this.pole = pole;
        this.obwod = obwod;
        this.ilosc_bokow = ilosc_bokow;
    }

    Okrag(int pole, int obwod, int ilosc_bokow){
      super(pole, obwod, ilosc_bokow);
    }

    public int getPromien() {
        return promien;
    }

    public int getSrednica() {
        return srednica;
    }

    public String getKolor() {
        return kolor;
    }

    public void setPromien(int promien){
        this.promien = promien;
    }

    public void setSrednica(int srednica){
        this.srednica = srednica;
    }

    public void setKolor(String kolor){
        this.kolor = kolor;
    }

    private void writeObject(ObjectOutputStream stream) throws IOException {
        stream.writeInt(pole);
        stream.writeInt(obwod);
        stream.writeInt(ilosc_bokow);
        stream.writeInt(promien);
        stream.writeInt(srednica);
        stream.writeUTF(kolor);
    }

    private void readObject(ObjectInputStream stream) throws IOException, ClassNotFoundException {
        pole = stream.readInt();
        obwod = stream.readInt();
        ilosc_bokow = stream.readInt();
        promien = stream.readInt();
        srednica = stream.readInt();
        kolor = stream.readUTF();
    }

    public String toString(){
        return "<html>INFORMACJE O FIGURZE: <br/> Okrąg" + "<html><br/><html/>" + "Pole: " + pole
                + "<html><br/><html/>" + "Obwód: " + obwod + "<html><br/><html/>" + "Ilość boków: " + ilosc_bokow
                + "<html><br/><html/>" + "Promień: " + promien + "<html><br/><html/>" + "Średnica: " + srednica
                + "<html><br/><html/>" + "Kolor: " + kolor;
    }
}
