from turtle import *
from duze_cyfry import daj_cyfre
import random

ht()
speed(0)
colormode(255)#RGB 

def zapis(lista):
    ile_cyfr=len(lista)
    wynik=[]
    for i in range(ile_cyfr):
        wynik=wynik+[daj_cyfre(lista[i])]
    return wynik

def kwadrat(kolor):
    color(kolor, kolor) #linie środek
    begin_fill()
    for _ in range(4):
        forward(15)
        right(90)
    end_fill()

def los_kolor(ilosc):
    wynik = []
    for i in range(ilosc):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        kolor = (r, g, b)
        wynik += [kolor]
    return wynik

def wypisanie(wynik):
    lista_kolorow = los_kolor(len(wynik))
    for i in range(5):
        for j in range(len(wynik)):
            for h in range(5):
                if(wynik[j][i][h]=="#"):
                    kwadrat(lista_kolorow[j%len(wynik)])
                else:
                    penup() #nie rysuje
                    kwadrat((255,255,255))
                    pendown()
                penup()    
                forward(15)
                pendown()
            penup()
            forward(10)
            pendown()
        penup()
        right(90)
        forward(15)
        right(90)
        forward(len(wynik)*5*15+10*len(wynik))
        right(180)
        pendown()
        
n=input('Podaj liczbe: ')
lista=[int(e) for e in n] # bierze kazda cyfre osobno i wpisuje do listy !n to string!
wynik=zapis(lista)
wypisanie(wynik)
done()