package com.company;
//pracownia 5 zad 1
import java.util.Collections; //aby użyć interfejs Comparable<T>

public interface Swierzaki extends Comparable<Swierzaki> { //żeby wszystkie podklasy klasy Swierzaki można było porównywać
    int getAtrakcyjnosc(); //atrakcyjośc od 1-10

    @Override //nadpisanie zamiast virutal
    int compareTo(Swierzaki obj);
}
