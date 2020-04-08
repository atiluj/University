class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

def wypisz(lis):
    while lis.next != None:
        print(lis.val)
        lis=lis.next

#Zadanie 2
def dodac_na_koniec(lis, wartosc):
    first = lis
    if lis == None:
        lis = ListItem(wartosc)
    else:
        while lis.next != None:
            lis = lis.next
        lis.next = ListItem(wartosc)
    return first

lis = ListItem(1)
first = dodac_na_koniec(lis,2)
wypisz(first)