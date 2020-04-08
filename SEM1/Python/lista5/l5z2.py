from turtle import *

speed(0)
ht()

def rysuj_kolo(srednica,kolor):
    fillcolor(kolor)
    begin_fill()
    circle(srednica)
    end_fill()

lista_kolorow = ["yellow", "blue", "green"]
srednica = 150
for i in range(13):
    kolor = lista_kolorow[i%3]
    rysuj_kolo(-srednica, kolor)
    srednica -= 10
done()