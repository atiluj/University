package com.company; //pracownia 6 zad 2
import java.util.Collections;

public class Main2 {

    public static void main(String[] args){

        List<Integer> m1 = new List<>();
        List<Integer> m2 = new List<>();
        List<Integer> m3 = new List<>();
        List<Integer> m4 = new List<>();
        m1.addAll(Collections.singleton(10));
        m1.addAll(Collections.singleton(11));
        m1.addAll(Collections.singleton(22));
        m2.addAll(Collections.singleton(5));
        m2.addAll(Collections.singleton(6));
        m2.addAll(Collections.singleton(7));
        m2.addAll(Collections.singleton(8));
        m2.addAll(Collections.singleton(9));
        m3.addAll(Collections.singleton(22));
        m3.addAll(Collections.singleton(23));
        m3.addAll(Collections.singleton(10));
        m4.addAll(Collections.singleton(10));
        m4.addAll(Collections.singleton(22));

        System.out.println("Wypisanie m1     " + m1);
        System.out.println("Wypisanie m2     " + m2);
        System.out.println("Wypisanie m3     " + m3);
        System.out.println("Wypisanie m4     " + m4);

        System.out.println("Czy 9 jest w m1:  " + m1.contains(9));
        System.out.println("Czy 9 jest w m2:  " + m2.contains(9));

        System.out.println("Czy zadzialalo dodanie m1 do m2: " + m2.addAll(m1));
        System.out.println("Zobaczym jak teraz wygląda m2:     " + m2);

        System.out.println("Czy zadzialalo usniecie elementow:    " + m2.removeAll(m2));
        System.out.println("Zobaczym jak teraz wygląda m2:     " + m2);

        System.out.println("Tak wygląda m1:     " + m1);
        System.out.println("Tak wygląda m3:     " + m3);
        System.out.println("retainAll: " + m1.retainAll(m3));
        System.out.println("Zobaczym jak teraz wygląda m1:     " + m1);
        System.out.println("Zobaczym jak teraz wygląda m3:     " + m3);

        System.out.println("Czy m1 zawiera elementy m4:     " + m1.containsAll(m4));

        System.out.println("Zobaczym jak teraz wygląda m1:     " + m1);
        m1.clear();
        System.out.println("Zobaczym jak wygląda m1 po wyczyszceniu:     " + m1);

        m3.add(21);
        m3.remove(10);

        System.out.println("Tak wyglada m3 po dodaniu '21' i usunieciu '10':       " + m3);
    }
}
