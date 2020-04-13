package com.company;//Julita Osman 314323 pracowania 5 zadanie 2

public class Operacje extends Wyrazenie { //klasa operacja dziedzcząca z klasy Wyrażenie
    Wyrazenie w1; //poddrzewo
    Wyrazenie w2;
    String operand;

    Operacje(String operator, Wyrazenie e1, Wyrazenie e2){ //konstruktor
        if (operator == "/" && e2.oblicz() == 0)
            throw new IllegalArgumentException("Argument divisor is 0 :("); //blad dzielenia przez 0
        w1 = e1;
        w2 = e2;
        operand = operator;
    }

    public int oblicz(){
        switch (operand){
            case "+":
                return w1.oblicz() + w2.oblicz();
            case "-":
                return w1.oblicz() - w2.oblicz();
            case "*":
                return w1.oblicz() * w2.oblicz();
            case "/":
                return w1.oblicz() / w2.oblicz();
            default:
                throw new IllegalArgumentException("Nieznany operator."); //gdy nieznany operator
        }
    }

    public String toString() {
        switch (operand) {
            case "+":
                return "(" + w1 + " + "  + w2 + ") ";
            case "-":
                return "(" + w1 +" - "  + w2+ ") ";
            case "*":
                return "(" + w1 + " * " +  w2 + ") ";
            case "/":
                return "(" + w1 + " / "  + w2 + ") ";
            default:
                throw new IllegalArgumentException("Nieznany operator.");
        }
    }
}