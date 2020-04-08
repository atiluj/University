package com.company;

public class Main {

    public static void main(String[] args) {
	    Gruszka g1 = new Gruszka("Gosia", 4, 10009);
        System.out.print(g1);
        Gruszka g2 = new Gruszka("Genia", 5, 1209);
        System.out.print(g2);
        Brokul b1 = new Brokul("Bartek", 2, 1212123209);
        System.out.print(b1);
        Ogoreczek o1 = new Ogoreczek("Olusia", 10, 1212123209);
        System.out.print(o1);
        Dynia d1 = new Dynia("Dawidek", 1, 1212123209);
        System.out.print(d1);

        KolekcjaSwierzakow ko1 = new KolekcjaSwierzakow();
        ko1.add(g1);
        ko1.add(g2);
        ko1.add(b1);
        ko1.add(o1);
        ko1.add(d1);
        System.out.print(ko1);

    }
}
