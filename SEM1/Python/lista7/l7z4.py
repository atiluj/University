from turtle import *

tracer(0,1)

kolory=["blue","green","yellow","red","orange",'purple']

def kwadrat(bok,kolor):
    for e in kolory:
        if e[0]==kolor:
            kolor=e
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
      fd(bok)
      rt(90)
    end_fill()
    
def murek(s,bok,kolor):
    licznik = 0
    for a in s:
        if a == 'f':
            kwadrat(bok,kolor[licznik%len(kolor)])
            fd(bok)
            licznik +=1
        elif a == 'b':
            kwadrat(bok,kolor[licznik%len(kolor)])
            fd(bok) 
            licznik +=1        
        elif a == 'l':
            bk(bok) #back
            lt(90) 
        elif a == 'r':
            rt(90)
            fd(bok)

ht()

#tracer(0,0) # szybkie rysowanie     
#murek('fffffffffrfffffffffflfffffffffrfffffl',10, "brg")    
#murek(4 * 'fffffr', 14, "rgo")    
murek('ffffrfrffflflfffrfrfff',10, 'brg')
update() # uaktualnienie rysunku
pu()
goto(-100,100)
pd()
murek('ffffffrfffffrffffrfffrffrf',10, 'bgyorp')
done()

input()
