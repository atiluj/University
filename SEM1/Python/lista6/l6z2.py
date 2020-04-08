"""lista=[]
for wiersz in open('slowa.txt'):
    wiersz = wiersz[:-1] # usuń ostatni element czyli usun eneter
    slowo = wiersz[::-1]
    lista = lista + [wiersz] + [slowo]
    #print (slowo, wiersz)"""
wynik=[]
lista = open('slowa.txt').split()
print(lista)
for wiersz in lista:
    slowo=wiersz[::-1]
    wynik=wynik+[slowo]+[wiersz]
lista.sort()
#print(lista)
for i in range(len(lista)-1):
    if lista[i]==lista[i+1]:
        print(lista[i])
        print(lista[i+1])

