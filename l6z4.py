def podziel(napis):	
	wynik=[]
	napis=napis+" "
	tmp=""
	i=0
	while(i<len(napis)-1):
		if napis[i]!=" ":
			tmp=tmp+napis[i]
			i=i+1
		if napis[i]==" ":
			if tmp!="":
				Lista_slow.append(tmp)
			tmp=""
			i=i+1
	return Lista_slow

def podziel(napis):
    wynik=[]
    napis=napis+" "
    slowo=""
    for i in range(len(napis)):
        if napis[i]!=" ":
            slowo=slowo+napis[i]
        else: 
            if napis[i]==" ":
                if slowo!="":
                    wynik=wynik+[slowo]
                    slowo=""
    return wynik
                

napis="  Marysia lubi czarne pieczywo "
wynik=podziel(napis)
print(wynik)
