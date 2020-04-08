def stworzenie_listy(n):
    lista=[]
    for i in range(2,n+1):
        lista = lista + [i]
    return lista

def erastotenes(n):
    lista=stworzenie_listy(n)
    for i in range (len(lista)):  # moze byc bez tego +1
        if(lista[i]!=0):
            dzielnik=lista[i]
            j=i
            for j in range (len(lista)):   #  moze vyc bez tego +1
                if(lista[j]%dzielnik==0):
                    lista[j]=0
    return lista

def palindorm(n):
    erastotenes(n)
    for i in range(len(lista):
        if(lista[i!=0]):
            pal=lista[i]
            for j in range(len(lista)):
                if(x=)







n=int(input("Podaj liczbe: "))