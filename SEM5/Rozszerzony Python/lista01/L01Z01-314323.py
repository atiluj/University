from decimal import *

def vat_faktura(zakupy):
    length = len(zakupy)
    suma = 0.0
    for i in range(length):
        suma = suma + zakupy[i]
    return suma * 0.23
    
def vat_paragon(zakupy):
    length = len(zakupy)
    suma = 0.0
    for i in range(length):
        suma = suma + zakupy[i] * 0.23
    return suma


zakupy1 = [0.2, 0.5, 4.59, 6]

#print(vat_faktura(zakupy1))
#print(vat_paragon(zakupy1))
print("Dla zwykłych wyliczeń: ", vat_faktura(zakupy1) == vat_paragon(zakupy1))

#######################DECIMAL#########################################
#czy reprezentacja za pomocą klasy decimal daje inną odpowiedz?
getcontext().prec = 2

#print(Decimal(vat_faktura(zakupy1)) * Decimal(1))
#print(Decimal(vat_paragon(zakupy1)) * Decimal(1))
print("Dla wyliczeń z użyciem DECIMAL:", Decimal(vat_faktura(zakupy1)) * Decimal(1) == Decimal(vat_paragon(zakupy1)) * Decimal(1))
