package com.company; //PRACOWNIA 7

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class Wyszukaj {
    ArrayList<Figura> kolekcja;
    String hello = "Witaj!";
    JFrame mainFrame;
    String pol = "WYBIERZ FIGURĘ KTÓREJ SZUKASZ:";
    JLabel polecenie;

    Wyszukaj(ArrayList<Figura> kolekcja){
        mainFrame = new JFrame();
        mainFrame.setLayout(null);
        mainFrame.setSize(600, 600);
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.kolekcja = kolekcja;
        String[] lp = new String[kolekcja.size()];//liczby porządkowe
        for(int i = 0; i < kolekcja.size(); i++){
            int x = i + 1;
            lp[i] = "Figura " + x;
        }
        JComboBox lpp = new JComboBox(lp);
        lpp.setBounds(250,130,100,50);

        polecenie = new JLabel(pol, SwingConstants.CENTER);
        polecenie.setBounds(150,70, 300,50);

        JButton exit = new JButton("WRÓĆ");
        exit.setBounds(400,450,100,50);
        exit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                mainFrame.dispose();
            }
        });
        mainFrame.add(exit);

        JButton wyswietl = new JButton("WYŚWIETL");
        wyswietl.setBounds(250, 200, 100, 50);
        JLabel nazwa = new JLabel();
        nazwa.setBounds(100, 115, 500,500);
        wyswietl.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                int idx = lpp.getSelectedIndex();

                String info = kolekcja.get(idx).toString();
                nazwa.setText(info);
                System.out.println(info);

            }
        });




        mainFrame.add(nazwa);
        mainFrame.add(wyswietl);
        mainFrame.add(lpp);
        mainFrame.add(polecenie);
        mainFrame.setVisible(true);
    }

}
