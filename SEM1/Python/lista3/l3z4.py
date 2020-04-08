from turtle import* #importuje wszystkie rzeczy z turtla
speed(0)#szybko
#ht()#nie widać strzałki 
for _ in range(9):
    dl = 80 #dlugosc jednej lini
    for _ in range (25):
        forward(dl) #idzie do przodu
        right(180) #obraca sie o 180 stopni
        forward(dl) # wraca na to samo miejsce
        right(181.6) #360/(9*25)=1,6
        dl=dl+4

done()