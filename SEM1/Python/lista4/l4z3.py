import random

def lista_liczb(n):
    liczby=[]
    for i in range (n):
        liczby = liczby + [i]
    return liczby 

def randperm(n):
    liczby=lista_liczb(n)
    wynik=[]
    t=n
    for i in  range(n):
        t=t-1
        los=random.randint(0,t) #losuje
        wynik =wynik + [liczby[los]]
        liczby[los], liczby[t] = liczby[t], liczby[los]
    return wynik

def wywolanie(n):
    for i in range(1,3):  #poda 3 permutacje
        print("permutacja ",i)
        print(randperm(n))

n= int(input("podaj n: "))
wywolanie(n)