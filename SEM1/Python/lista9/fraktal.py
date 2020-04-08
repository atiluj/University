from turtle import *

def koch(glebokosc, dlugosc):
    if glebokosc == 0:
        forward(dlugosc)
    else:
        koch(glebokosc-1, dlugosc/3)
        left(60)
        koch(glebokosc-1, dlugosc/3)
        right(120)
        koch(glebokosc-1, dlugosc/3)
        left(60)
        koch(glebokosc-1, dlugosc/3)

pu()
goto(-200,-200)
pd()

koch(3, 400)
        
done()
    


    