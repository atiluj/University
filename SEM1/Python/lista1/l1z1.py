#######################################
# hello.py
######################################               #komenatrz liniowy

"""
To jest pierwszy program
Otwieramy go tym komentarzem                         #komenatrz przedziałowy
"""

print ("Witamy na WdP!")

# Uwaga: dwukropek mówi o tym
# że poniżej będzie blok instrukcji
# (z wcięciem)

for i in range(10):                     #i=0 i<10
    print ('Bardzo serdecznie!') 
    print ('Bardzo, bardzo')
    

print (10 * 'Naprawde\n') 

# przykładowe konwersje typów

print (str(100) + '22')       #10022
print (100 + int('22'))       #122

########################################
# Dodatkowe parametry funkcji print
########################################

    
for i in range(5):
    print ("Ala ma kota", end=" ")        #end print daje nowa linie

print ()                                  #\n
    
for i in range(11, 16):                   #i=11  i<16
    print ("Ala ma" + str(i), "kotów", sep='**')        
    
for i in range(0, 21, 3):                 #i=0  i<21   i+3
    print (i, sep=' ')
    
print ()   
    
#############################################
# Trójmian kwadratowy, wersja z problemami
#############################################    
    
from math import sqrt                     #importowanie z biblioteki

a = input('Podaj a: ')                    #podaje uzytkownik
b = input('Podaj b: ')                    #to jest w stringu
c = input('Podaj c: ')

a = float(a) # nie bardzo elegancko       #zamienienie na float
b = float(b) # bo zmienamy typ
c = float(c) # ale za to jest poprawne

delta = b ** 2 - 4 * a * c

if delta < 0:
    print ('Nie ma rozwiązań rzeczywistych')
else: # delta >= 0
    if delta == 0: 
        print ('x1 = x2 =', -b / (2*a))
    else: # delta > 0
        x1 = (-b - delta ** 0.5) / (2*a) # opcja 1
        x2 = (-b + sqrt(delta)) / (2*a)  # opcja 2   
        print ('x1 =', x1)
        print ('x2 =', x2)   

#############################################
# Trójmian kwadratowy, wersja preferowana
#############################################    
    
from math import sqrt

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))

delta = b ** 2 - 4 * a * c

if a == 0:
    print ('To nie jest równianie kwadratowe!')
elif delta < 0:
    print ('Nie ma rozwiązań rzeczywistych')
elif delta == 0:
    print ('x1 = x2 =', -b / (2*a))
else: # delta > 0
    x1 = (-b - sqrt(delta)) / (2*a) 
    x2 = (-b + sqrt(delta)) / (2*a)   
    print ('x1 =', x1)
    print ('x2 =', x2)   

##############################################
# Potęga i definiowanie funkcji
##############################################

# zakładamy, że n >= 0
def potega(a, n):                          #funckja
    wynik = 1
    for i in range(n):
        wynik *= a # to samo: wynik = wynik * a
    return wynik
    
# funkcja może zwracać wartości różnych typów
# (oczywiście staramy się nie nadużywać tej możliwości)    

def rozne_typy(n):
    opcja = n % 3
    if opcja == 0:
        return n / 13          #dzielenie całkowite to //
    elif opcja == 1:           #elif = else if
        return 'Hej' + str(n)
    elif opcja == 2:
        return 1 == 1
    else:
        return 'To się nie powinno zdarzyć!'            
    
for i in range(10):
    print (i, potega(2, i))        
    
for i in range(10):
    print (rozne_typy(i))    
    
##############################################
# Pętla while, break i rzucanie kostką
##############################################
            
import random

def kostka():
    return random.randint(1,6)           #ranodmowe liczby od 1 do 6
    
for i in range(0):                       #nic nie wypisze
    print (kostka(), end=' ')
        
print ()

while True:
    k1 = kostka()
    k2 = kostka()
    if k1 == 6 and k2 == 6:
        print (k1, k2)    
        print ('Sukces')
        break
    else:
        print (k1, k2) 