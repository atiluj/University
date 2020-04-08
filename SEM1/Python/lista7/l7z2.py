from turtle import *
import random

colormode(255)
ht()
tracer (10,1) 

def wczytanie():
    wynik=[]
    for linia in open('obrazek.txt'):
        wiersz=[]
        linia=linia.split() #zamiast spacji przeciniki
        for element in linia:
            wiersz += [eval(element)] #zwraca wartość np.1+3 to zwróci 4
        wynik += [wiersz] # lista list
    return wynik

def kwadrat(kolor,bok):
    fillcolor(kolor) #color(kolor, kolor)
    begin_fill()
    for i in range(4):
        forward(bok)
        right(90)
    end_fill()

def narysuj(lista, bok):
    pu()
    los=[] #zawriera współrzedne
    for i in range(len(lista[0])):
        for j in range(len(lista)):
            los +=[[i,j]]
    for _ in range((len(lista[0])) * (len(lista))):
        l = random.choice(los)
        los.remove(l) # to co wylosowałam usuwam zeby nie wylosowac tego jeszcze raz
        goto(-300+(bok*l[1]),300-(bok*l[0]))
        kwadrat(lista[l[1]][l[0]],bok)


lista = wczytanie()
narysuj(lista,10) # 10 bok 

done()