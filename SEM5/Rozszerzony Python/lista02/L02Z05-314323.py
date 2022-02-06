def kompresja(tekst):
    result = []
    i = 0

    while i<len(tekst):
        sum = 1

        if i<len(tekst)-1:
            
            while tekst[i] == tekst[i+1]:
                sum += 1
                if i+1 == len(tekst)-1:
                    i += 1
                    break
                i += 1
            
        new = (sum, tekst[i])
        result.append(new)
        i = i + 1

    return result


def dekompresja(tekst_skompresowany):
    result = ""
    for i in range(len(tekst_skompresowany)):
        result += tekst_skompresowany[i][0]*tekst_skompresowany[i][1] 
    return result

# źródło tekst - Śpiewnik Clemensianum
print("      -----1-----")
print(kompresja("Wielkie są dzieła Twej potęgi Panie i godne podziwu Twoje miłosierdzie! Alleluja, alleluja, alleluja!"))
print("      -----2-----")
print(kompresja("aaabbcccccd ddd"))
print("\n")
print(dekompresja([(3, 'a'), (2, 'b'), (5, 'c'), (1, 'd'), (1, ' '), (3, 'd')]))
print(dekompresja([(1, 'W'), (1, 'i'), (1, 'e'), (1, 'l'), (1, 'k'), (1, 'i'), (1, 'e'), (1, ' '), (1, 's'), (1, 'ą'), (1, ' '), (1, 'd'), (1, 'z'), (1, 'i'), (1, 'e'), (1, 'ł'), (1, 'a'), (1, ' '), (1, 'T'), (1, 'w'), (1, 'e'), (1, 'j'), (1, ' '), (1, 'p'), (1, 'o'), (1, 't'), (1, 'ę'), (1, 'g'), (1, 'i'), (1, ' '), (1, 'P'), (1, 'a'), (1, 'n'), (1, 'i'), (1, 'e'), (1, ' '), (1, 'i'), (1, ' '), (1, 'g'), (1, 'o'), (1, 'd'), (1, 'n'), (1, 'e'), (1, ' '), (1, 'p'), (1, 'o'), (1, 'd'), (1, 'z'), (1, 'i'), (1, 'w'), (1, 'u'), (1, ' '), (1, 'T'), (1, 'w'), (1, 'o'), (1, 'j'), (1, 'e'), (1, ' '), (1, 'm'), (1, 'i'), (1, 'ł'), (1, 'o'), (1, 's'), (1, 'i'), (1, 'e'), (1, 'r'), (1, 'd'), (1, 'z'), (1, 'i'), (1, 'e'), (1, '!'), (1, ' '), (1, 'A'), (2, 'l'), (1, 'e'), (1, 'l'), (1, 'u'), (1, 'j'), (1, 'a'), (1, ','), (1, ' '), (1, 'a'), (2, 'l'), (1, 'e'), (1, 'l'), (1, 'u'), (1, 'j'), (1, 'a'), (1, ','), (1, ' '), (1, 'a'), (2, 'l'), (1, 'e'), (1, 'l'), (1, 'u'), (1, 'j'), (1, 'a'), (1, '!')]))
print(dekompresja(kompresja("Wielkie są dzieła Twej potęgi Panie i godne podziwu Twoje miłosierdzie! Alleluja, alleluja, alleluja!")))








