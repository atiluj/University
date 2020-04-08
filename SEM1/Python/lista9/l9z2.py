from turtle import *

speed(5)
def trojkat(bok): 
    for _ in range(3):
        fd(bok)
        lt(120)


def trojkatSierpinskiego(n,bok):
    trojkat(bok)
    if n>0:
        trojkatSierpinskiego(n-1,bok/2)
        fd(bok/2)
        trojkatSierpinskiego(n-1,bok/2)
        lt(120)
        fd(bok/2)
        rt(120)
        trojkatSierpinskiego(n-1,bok/2)
        rt(120)
        fd(bok/2)
        lt(120)

trojkatSierpinskiego(3,300)
done()