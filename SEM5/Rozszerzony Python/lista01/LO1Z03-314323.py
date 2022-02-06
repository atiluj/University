def tabliczka(lista1, lista2, ile):
    wynik = []
    for i in range(ile):
        wynik.append([])

    for i in range(ile):
        for j in range(ile):
            wynik[i].append(lista1[i]*lista2[j])

    begin = ''
    max2 = max(lista2)
    max_len = len(str(max2))
    for i in range(max_len + 3):
        begin = begin + ' '
        
    for i in range(ile):
        max_len = len(str(max(wynik[i])))
        for j in range(max_len - len(str(lista1[i]))):
            begin = begin + ' '
        begin = begin + str(lista1[i])
        begin = begin + '  '
    
    print(begin)
    print('-' * len(begin))

    for j in range(ile):
        begin = ''
        
        for i in range(ile):
            if i == 0:
                max2 = max(lista2)
                max_len = len(str(max2))
                for k in range(max_len - len(str(lista2[j]))):
                    begin = begin + ' '
                begin = begin + str(lista2[j])
                begin = begin + ' | '
            max2 = max(wynik[i])
            max_len = len(str(max2))
            for k in range(max_len - len(str(wynik[i][j]))):
                begin = begin + ' '
            begin = begin + str(wynik[i][j])
            begin = begin + '  '
        print(begin)

    print('\n')

#PRZYKŁAD
print("\n P R Z Y K Ł A D \n")
tabliczka([1, 10, 12, 4, 5],[5, 100, 11, 9, 0], 5)

#WPISZ WŁASNE
ile = int(input('Ile liczb będzie w każdej z list? '))
print('Podaj po', ile, 'liczb dla każdej z dwóch list ')

lista1 = []
lista2 = []
for i in range(ile):
    x = int(input('Podaj liczbe do listy pierwszej: '))
    lista1.append(x)
for i in range(ile):
    x = int(input('Podaj liczbe do listy drugiej: '))
    lista2.append(x)
print('\n')

#WPISZ WŁASNE
tabliczka(lista1, lista2, ile)
