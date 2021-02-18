package com.company; //Julita Osman 314323 pracownia 6 zadanie 5
import java.util.Arrays; //This class provides static methods to dynamically create and access Java arrays.

public class Main{

    public static void main(String[] args) throws InterruptedException {

        int[] tab = {65, 20, 1000, 12, 3, 123, 23, 5, 10};
        //printall(tab);
        MergeSort sort = new MergeSort(tab);
        sort.start();

        sort.join();

        //gdyby nie throws InterruptedException to wywolanie sort.join() wyglądało by tak

        //try{ //sprobuj to zrobić,
        sort.join();
        //} catch(Exception except){ //a jak sie nie uda to przechwyć wyjątek
        //}

        printall(tab);
    }

    private static void printall(int[] tab) {
        System.out.print("[");
        Arrays.stream(tab).forEach(e -> System.out.print(e + ", "));
        System.out.println("\b\b]");
    }
}
