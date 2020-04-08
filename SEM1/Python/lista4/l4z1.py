from turtle import *
#ht()
speed(0)
colormode(255)
g=255 #green
bok=1 
for i in range(18):
    for _ in range(bok):
        fillcolor(255, int(g), 102)
        begin_fill() #od tąd koloruje
        for _ in range(4): #bo kwadrat ma 4 boki
            forward(20)
            right(90)
        end_fill() #kończy kolorowac w tym kolorze
        g = g - 1.3
        forward(20)
    right(90)
    forward(20)
    bok=bok+1

done()

