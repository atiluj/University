package com.company; //PRACOWNIA 7

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class Edytor2 extends Edytor {
    String pol = "WYBIERZ FIGURE KTORA CHCESZ EDYTOWAC:";
    JLabel polecenie;
    String war = "MOŻESZ EDYTOWAĆ TYLKO WARTOSCI FIGURY!";
    JLabel warnning;

    Edytor2(ArrayList<Figura> kolekcja){
        super(kolekcja);

        String[] lp = new String[kolekcja.size()];//liczby porządkowe
        for(int i = 0; i < kolekcja.size(); i++){
            int x = i + 1;
            lp[i] = "Figura " + x;
        }
        JComboBox lpp = new JComboBox(lp);
        lpp.setBounds(380,20,150,50);

        polecenie = new JLabel(pol, SwingConstants.CENTER);
        polecenie.setBounds(85,20, 300,50);
        warnning = new JLabel(war, SwingConstants.CENTER);
        warnning.setBounds(80,40, 300,50);

        zapisz.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                int idx = lpp.getSelectedIndex();

                if(kolekcja.get(idx) instanceof Trojkat){
                    String strPole = poleText.getText();
                    int intPole = Integer.parseInt(strPole);
                    String strObwod = obwodText.getText();
                    int intObwod = Integer.parseInt(strObwod);
                    String strIlosc_bokow = ilosc_bokowText.getText();
                    int intIlosc_bokow = Integer.parseInt(strIlosc_bokow);
                    String strWysokosc = wysokoscText.getText();
                    int intWysokosc = Integer.parseInt(strWysokosc);
                    String strPodstawa = podstawaText.getText();
                    int intPodstawa = Integer.parseInt(strPodstawa);
                    String strBarwa = barwaText.getText();
                    ((Trojkat) kolekcja.get(idx)).setWysokosc(intWysokosc);
                    ((Trojkat) kolekcja.get(idx)).setPodstawa(intPodstawa);
                    ((Trojkat) kolekcja.get(idx)).setBarwa(strBarwa);
                }
                else if (kolekcja.get(idx) instanceof Okrag) {
                    String strPole = poleText.getText();
                    int intPole = Integer.parseInt(strPole);
                    String strObwod = obwodText.getText();
                    int intObwod = Integer.parseInt(strObwod);
                    String strIlosc_bokow = ilosc_bokowText.getText();
                    int intIlosc_bokow = Integer.parseInt(strIlosc_bokow);
                    String strPromien = promienText.getText();
                    int intPromien = Integer.parseInt(strPromien);
                    String strSrednica = srednicaText.getText();
                    int intSrednica = Integer.parseInt(strSrednica);
                    String strKolor = kolorText.getText();
                    ((Okrag) kolekcja.get(idx)).setPromien(intPromien);
                    ((Okrag) kolekcja.get(idx)).setSrednica(intSrednica);
                    ((Okrag) kolekcja.get(idx)).setKolor(strKolor);
                    kolekcja.get(idx).setIlosc_bokow(intIlosc_bokow);
                    kolekcja.get(idx).setPole(intPole);
                    kolekcja.get(idx).setObwod(intObwod);
                }
            }
        });


        mainFrame.add(polecenie);
        mainFrame.add(warnning);
        mainFrame.add(lpp);
        mainFrame.setVisible(true);
    }
}
