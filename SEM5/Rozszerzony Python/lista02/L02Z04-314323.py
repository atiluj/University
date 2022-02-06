import random

def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    result = []
    i = 0
    while i < len(tekst):
        start = i
        length = 0
        while tekst[i] != " ":
            i += 1
            length += 1
            if(i == len(tekst)):
                break
        end = i
        i += 1

        if length <= dl_slowa:
            new = (start, end-1)
            result.append(new)
        else:
            tekst = tekst[:start] + tekst[end+1:]
            i = start  

    #print(result)
    
    if len(result)>liczba_slow:
        delete = len(result) - liczba_slow
        toDelete = []
        i=0
        while i < delete:
            num = random.randint(0, len(result)-1)
            if toDelete.count(num) == 0:
                toDelete.append(num)
                i+=1
        toDelete.sort()

        for i in range(len(toDelete)):
            k = len(toDelete) - i - 1
            start = result[toDelete[k]][0]
            end = result[toDelete[k]][1]
            if start == 0:
                tekst = tekst[end+2:]
            elif end == len(tekst):
                tekst = tekst[end+1:]
            else: tekst = tekst[:start-1] + tekst[end+1:]

    return tekst
print("Tekst oryginalny = al asjdjasidjaijdsijasd asjidajsdja ajsidjaijdsijaidjisa")
print("Mają zostać conajwyżej", 2, "słowa, długości conajwyżej ", 10)
print(uprosc_zdanie("al asjdjasidjaijdsijasd asjidajsdja ajsidjaijdsijaidjisa", 10, 2))
print("--------------------------------------------------------------------------")
print("Tekst oryginalny = aaaaaa bb cccc sddd")
print("Mają zostać conajwyżej", 3, "słowa, długości conajwyżej ", 2)
print(uprosc_zdanie("aaaaaa bb cccc sddd", 2, 3))
print("--------------------------------------------------------------------------")
print("Tekst oryginalny = abca abbb bb assss dcccc sddd")
print("Mają zostać conajwyżej", 4, "słowa, długości conajwyżej ", 4)
print(uprosc_zdanie("abca abbb bb assss dcccc sddd", 4, 4))
print("--------------------------------------------------------------------------")
print("Tekst oryginalny = abca abbb bb assss dcccc sddd")
print("Mają zostać conajwyżej", 3, "słowa, długości conajwyżej ", 4)
print(uprosc_zdanie("abca abbb bb assss dcccc sddd", 4, 3))
print("--------------------------------------------------------------------------")
print("Tekst oryginalny = abcde alala sss aksjdne aksoanwjed")
print("Mają zostać conajwyżej", 3, "słowa, długości conajwyżej ", 12)
print(uprosc_zdanie("abcde alala sss aksjdne aksoanwjed", 12,3))
print("--------------------------------------------------------------------------")
print("Tekst oryginalny = Podział peryklinalny inicjałów wrzecionowatych kambium charakteryzuje się ścianą podziałową inicjowaną w płaszczyźnie maksymalnej.")
print("Mają zostać conajwyżej", 5, "słowa, długości conajwyżej ", 10)
print(uprosc_zdanie("Podział peryklinalny inicjałów wrzecionowatych kambium charakteryzuje się ścianą podziałową inicjowaną w płaszczyźnie maksymalnej.", 10, 5))
print("--------------------------------------------------------------------------")


#fragment ksiązki Adama Mickiewicza - Pan Tadusz, pdf dostępny https://wolnelektury.pl/media/book/pdf/pan-tadeusz.pdf
print("\nPRZYKŁADY DLA TESKTU LITERACKIGO - Pan Tadeusz - Adam Mickiewicz")
fragment = "Biegał po całym domu i szukał komnaty Gdzie mieszkał dzieckiem będąc przed dziesięciu laty. Dom Kobieta Wchodzi cofnął się, toczył zdumione źrenice Po ścianach: w teń komnacie mieszkanie kobiéce! Któż by tu mieszkał? Stary stryj nie był żonaty; A ciotka w Petersburgu mieszkała przed laty. To nie był ochmistrzyni pokój? Fortepiano? Na nim nuty i książki wszystko porzucano Niedbale i bezładnie: nieporządek miły!"
print("Mają zostać conajwyżej", 15, "słowa, długości conajwyżej ", 20)
print(uprosc_zdanie(fragment, 20, 15))
print("--------------------------------------------------------------------------")
print("Mają zostać conajwyżej", 5, "słowa, długości conajwyżej ", 20)
print(uprosc_zdanie(fragment, 20, 5))
print("--------------------------------------------------------------------------")
print("Mają zostać conajwyżej", 20, "słowa, długości conajwyżej ", 20)
print(uprosc_zdanie(fragment, 20, 20))