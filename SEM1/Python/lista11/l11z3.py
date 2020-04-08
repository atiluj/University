Wyniki = [linia.split('\t') for linia in open('wyniki_wyborow.tsv')]
Mandaty = {} #słownik

#usunięcie znaku nowej linii i zamiana przecinków na kropki: 
for linia in Wyniki:
    linia[9] = linia[9][:-1]
    for i in range(3, len(linia)): 
        linia[i] = linia[i].replace(",",".") # aby mógł czytac float

for i in range(1, len(Wyniki)): # 0 jest nazwa # ilośc lini w pliu
    Ilorazy = []
    for j in range(3, len(Wyniki[i])): #od 3 są partie
        for k in range(1,int(Wyniki[i][2])+1): #Wynik[i][2]+1 to jest ilośc mandatów
            if Wyniki[i][j] != "–":
                Ilorazy.append((float(Wyniki[i][j])/k, Wyniki[0][j])) #Wynik[0][j]nazwa partii
    Ilorazy = sorted(Ilorazy)[::-1] #od najmniejszego [::-1]obraca czyli od największej
    for l in range(int(Wyniki[i][2])): # tyle razi ile mandatow
        if Ilorazy[l][1] not in Mandaty.keys():
            Mandaty[Ilorazy[l][1]] = 1
        else: 
            Mandaty[Ilorazy[l][1]] += 1

print(Mandaty)
