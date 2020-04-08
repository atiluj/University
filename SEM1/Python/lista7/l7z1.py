from turtle import *

colormode(255)
ht()
tracer (0,1) 

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
    color(kolor,kolor) #color(kolor, kolor)
    begin_fill()
    for i in range(4):
        forward(bok)
        right(90)
    end_fill()

def narysuj(lista, bok):
    pu()
    goto(-300,300)
    pd()
    for i in range(len(lista[0])): # szerokosc tablicy
        for j in range(len(lista)):
            kwadrat(lista[j][i],bok)
            forward(bok)
        penup()
        goto(-300,300-(i*bok))
        pendown()


lista = wczytanie()
narysuj(lista,10) # 10 bok 

done()