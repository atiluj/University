package com.company; //PRACOWNIA 7

public abstract class Figura{
    protected int pole = 0;
    protected int obwod = 0;
    protected int ilosc_bokow = 0;

    public int getPole(){
        return pole;
    }

    public int getObwod(){
        return obwod;
    }

    public int getIlosc_bokow(){
        return ilosc_bokow;
    }

    public void setPole(int pole){
        this.pole = pole;
    }

    public void setObwod(int obwod){
        this.obwod = obwod;
    }

    public void setIlosc_bokow(int ilosc_bokow){
        this.ilosc_bokow = ilosc_bokow;
    }

    Figura(int pole, int obwod, int ilosc_bokow){ //konsruktor
        this.pole = pole;
        this.obwod = obwod;
        this.ilosc_bokow = ilosc_bokow;
    }

    Figura(){} //potrzebne do konstruktora okręgu i trójkąta
}
