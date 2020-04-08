from turtle import *
from duze_cyfry import daj_cyfre
import random

ht()
tracer(0) # od razu wypisze efekt
colormode(255)

def tworzenie_listy(n):
    lista=[]
    for i in range(n*5):
        lista=lista+[[" "]*n*5]
    return lista

def spr_miejsce(x,y,cyfra,lista):
    for i in range(5):
        for j in range(5):
            if(cyfra[i][j]=='#' and lista[x][y]=='#'):
                return False
            y += 1
        x += 1
        y -= 5
    return True

def dopisz_cyfre(x,y,cyfra,lista):
    for i in range(5):
        for j in range(5):
            if(cyfra[i][j]=='#'):
                lista[x][y]='#'
            y += 1
        x += 1
        y -= 5
    return lista    

def los_kolor(x, y, lista):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    for i in range(5):
        for j in range(5):
            lista[x][y] = (r, g, b)
            y += 1
        x += 1
        y -= 5
    return lista 

def los_liczby(lista,n):
    lista_kolorow = tworzenie_listy(n)
    for i in range(n*5):
        L=random.randint(0,9)
        x=random.randint(0,n*5-5) # bo cufra ma szerokosc i wysokosc 5 i sie nie zmiesci
        y=random.randint(0,n*5-5)
        cyfra=daj_cyfre(L)
        if(spr_miejsce(x,y,cyfra,lista)==True):
            dopisz_cyfre(x,y,cyfra,lista)
            lista_kolorow = los_kolor(x, y, lista_kolorow)
    return lista, lista_kolorow

def kwadrat(kolor):
    fillcolor(kolor)
    begin_fill()
    for _ in range(4):
        forward(10)
        right(90)
    end_fill()


def wypisz_wynik(wynik,n, lista_kolorow):
    """pu()
    goto(-300,300) # teleportuje sie d
    pd()"""
    for i in range(n*5):
        for j in range(n*5):
            if(wynik[i][j]=='#'):
                kwadrat(lista_kolorow[i][j])
            penup()
            forward(10)
            pendown()
        penup()
        right(90)
        forward(10)
        right(90)
        forward(n*5*10)
        right(180)
        pendown()

n=random.randint(10,15)
lista=tworzenie_listy(n)
wynik , lista_kolorow =los_liczby(lista,n) #zwraca wynik i liste kolorow
wypisz_wynik(wynik,n, lista_kolorow)

done()