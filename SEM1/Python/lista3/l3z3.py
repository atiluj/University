def usun_nawiasy(napis):
    while ("(" in napis):
        n1 = napis.find("(")
        n2 = napis.find(")")
        nawias = napis[n1:n2+1]
        napis=napis.replace(nawias,"")
    return napis


napis=input("Podaj napis: ")
print(usun_nawiasy(napis))