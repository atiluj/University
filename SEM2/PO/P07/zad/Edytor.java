package com.company; //PRACOWNIA 7

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class Edytor {
    JFrame mainFrame;
    ArrayList<Figura> kolekcja;
    JRadioButton wyborOkrag;
    JRadioButton wyborTrojkat;
    String pol = "PODAJ DANE:";
    JLabel polecenie;
    JButton zapisz;
    JTextField poleText, obwodText, ilosc_bokowText, promienText, srednicaText, kolorText, wysokoscText, podstawaText, barwaText;

    Edytor(ArrayList<Figura> kolekcja){
        mainFrame = new JFrame();
        mainFrame.setLayout(null);
        mainFrame.setSize(600, 600);
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.kolekcja = kolekcja;
        wyborOkrag = new JRadioButton("Okrag");
        wyborTrojkat = new JRadioButton("Trojkat");
        wyborOkrag.setBounds(100, 230, 150, 20);
        wyborTrojkat.setBounds(360, 230, 150, 20);
        ButtonGroup wybor = new ButtonGroup();
        wybor.add(wyborOkrag);
        wybor.add(wyborTrojkat);

        polecenie = new JLabel(pol, SwingConstants.CENTER);
        polecenie.setBounds(135,70, 300,50);

        poleText = new JTextField("Podaj pole");
        poleText.setBounds(220, 125, 140, 20);
        obwodText = new JTextField("Podaj obwod");
        obwodText.setBounds(220, 155, 140, 20);
        ilosc_bokowText = new JTextField("Podaj ilosc bokow figury");
        ilosc_bokowText.setBounds(220, 185, 140, 20);
        promienText = new JTextField("Podaj promien");
        promienText.setBounds(100, 275, 100, 20);
        srednicaText = new JTextField("Podaj srednice ");
        srednicaText.setBounds(100, 305, 100, 20);
        kolorText = new JTextField("Podaj kolor");
        kolorText.setBounds(100, 335, 100, 20);
        wysokoscText = new JTextField("Podaj wysokosc");
        wysokoscText.setBounds(360, 275, 140, 20);
        podstawaText = new JTextField("Podaj wartosc podstawy");
        podstawaText.setBounds(360, 305, 140, 20);
        barwaText = new JTextField("Podaj barwe");
        barwaText.setBounds(360, 335, 140, 20);

        zapisz = new JButton("ZAPISZ");
        zapisz.setBounds(220, 400, 120,40);

        JButton exit = new JButton("WRÓĆ");
        exit.setBounds(220,460,120,40);
        exit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                mainFrame.dispose();
            }
        });
        mainFrame.add(exit);

        zapisz.addActionListener(new ActionListener() {  // co sie stanie po nacisnięciu 'zapisz'
            @Override
            public void actionPerformed(ActionEvent actionEvent) {

                if(wyborTrojkat.isSelected()){
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
                    kolekcja.add(new Trojkat(intWysokosc, intPodstawa, strBarwa, intPole, intObwod, intIlosc_bokow));
                }
                else {
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
                    kolekcja.add(new Okrag(intPole, intObwod, intIlosc_bokow, intPromien, intSrednica, strKolor));
                }

                mainFrame.dispose();
        }
        });

        mainFrame.add(poleText);
        mainFrame.add(obwodText);
        mainFrame.add(promienText);
        mainFrame.add(srednicaText);
        mainFrame.add(kolorText);
        mainFrame.add(podstawaText);
        mainFrame.add(barwaText);
        mainFrame.add(wysokoscText);
        mainFrame.add(ilosc_bokowText);
        mainFrame.add(zapisz);
        mainFrame.add(polecenie);
        mainFrame.add(wyborOkrag);
        mainFrame.add(wyborTrojkat);
        mainFrame.setVisible(true);
    }
}
