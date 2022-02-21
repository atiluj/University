package com.company; //PRACOWNIA 7

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class InterfejsGraficzny{
    ArrayList<Figura> kolekcja;
    String hello = "W I T A J !   WYBIERZ ODPOWIEDNI PRZYCISK: ";
    JFrame mainFrame; //glowne okienko
    JLabel invitation; //napis
    JButton dodajFigure;
    JButton wyszukajFigure;
    JButton edytujFigure;

    InterfejsGraficzny(ArrayList<Figura> kolekcja){
        this.kolekcja = kolekcja;
        mainFrame = new JFrame("Figury");
        //spr
        mainFrame.setLayout(null);
        mainFrame.setSize(600, 600);
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //przypisanie co ma robic przycisk 'zamknij'

        invitation = new JLabel(hello, SwingConstants.CENTER);
        invitation.setBounds(150,60, 300,50);
        //invitation.setBorder(BorderFactory.createLineBorder(Color.black));
        mainFrame.add(invitation);

        dodajFigure = new JButton("Dodaj figure");
        dodajFigure.setBounds(200, 130, 200, 60);
        dodajFigure.addActionListener(new ActionListener() { //po nacisnieciu
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                Edytor e1 = new Edytor(kolekcja);
            }
        });
        mainFrame.add(dodajFigure);

        wyszukajFigure = new JButton("Wyszukaj figure");
        wyszukajFigure.setBounds(200, 100+130, 200, 60);
        wyszukajFigure.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                Wyszukaj e2 = new Wyszukaj(kolekcja);
            }
        });
        mainFrame.add(wyszukajFigure);

        edytujFigure = new JButton("Edytuj figure");
        edytujFigure.setBounds(200, 100+230, 200, 60);
        edytujFigure.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                Edytor2 e3 = new Edytor2(kolekcja);
            }
        });
        mainFrame.add(edytujFigure);

        mainFrame.setVisible(true);
    }
}
