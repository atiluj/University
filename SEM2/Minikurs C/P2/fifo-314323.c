#include <stdio.h>
#include <stdlib.h>
// pracownia 1 zadanie 2 KOLEJKA FIFO
struct fifo
{
    int calkowita;
    float zmiennoprzecinkowa;
    char napis[50];
    int x,y;

    int typ; // bedzie przechowywac typ zmiennej (liczba calkowita, zmiennoprzecinkowa, napis lub pare liczb calkowitych)
};

struct fifo kolejka[10]; //utworzenie kolejki która ma miejsc na 10 elementów

int ile = 0; //ilosc elementow w tablicy

void push() // wrzucenie do kolejki
{
    int rodzaj;

    if (ile == 9) // jeœli kolejka jest pelna to nie mozemy dodaæ do niej kolejnego elementu
    {
        printf("Kolejka jest juz pelna. Nie mozesz dodac kolejnego elementu.\n");
        printf("----- \n");
        return;
    }

    printf("Wpisz: \n");
    printf("1 - jesli chcesz dodac liczbe calkowita \n");
    printf("2 - jesli chcesz dodac liczbe zmienoprzecinkowa \n");
    printf("3 - jesli chcesz dodac napis \n");
    printf("4 - jesli chcesz dodac pare \n");
    scanf("%d", &rodzaj);

    switch(rodzaj)
    {
    case 1: //calkowita
    {
        printf("Podaj liczbe calkowita: \n");
        scanf("%d", &kolejka[ile].calkowita);
        kolejka[ile].typ = 1; //zapamietuje jaki typ zostal w³o¿ony aby pamietac przy jego usuwaniu
        ile++;
        printf("----- \n");

        break;
    }
    case 2: //float
    {
        printf("Podaj liczbe zmiennoprzecinkowa: \n");
        scanf("%f", &kolejka[ile].zmiennoprzecinkowa);
        kolejka[ile].typ = 2;
        ile++;
        printf("----- \n");

        break;
    }
    case 3: //napis
    {
        printf("Podaj napis:  \n");
        scanf("%s", kolejka[ile].napis);
        kolejka[ile].typ = 3;
        ile++;
        printf("----- \n");

        break;
    }
    case 4: //para
    {
        printf("Podaj pare: \n");
        scanf("%d %d", &kolejka[ile].x, &kolejka[ile].y);
        kolejka[ile].typ = 4;
        ile++;
        printf("----- \n");

        break;
    }
    }
}

void pop()  //wyrzucanie z kolejki
{
    if (ile == 0)
    {
        printf("Kolejka jest pusta. Nie mozesz nic z niej usunac. \n");
        printf("----- \n");
        return;
    }
    {
        switch(kolejka[0].typ)
        {
        case 1:
        {

            printf("Usuwam: %d\n ", kolejka[0].calkowita);
            printf("----- \n");
            break;
        }
        case 2:
        {
            printf("Usuwam: %f\n ", kolejka[0].zmiennoprzecinkowa);
            printf("----- \n");
            break;
        }
        case 3:
        {

            printf("Usuwam: %s\n ", kolejka[0].napis);
            printf("----- \n");
            break;
        }
        case 4:
        {
            printf("Usuwam: %d, %d \n ", kolejka[0].x, kolejka[0].y);
            printf("----- \n");
            break;
        }
        }

        //usuwanie
        for (int i=0; i < ile; i++)
        {
            kolejka[i] = kolejka[i+1];
        }
        ile--;
    }
}


int main()
{
    while (1)
    {
        int operacja;
        printf("Wpisz \n");
        printf("1 - aby dodac element do kolejki\n");
        printf("2 - aby usunac element z kolejki\n");
        printf("3 - aby zakonczyc dzialanie programu\n");
        scanf("%d", &operacja);

        switch(operacja)
        {
        case 1:
        {
            push();
            break;
        }
        case 2:
        {
            pop();
            break;
        }
        case 3:
        {
            printf("Zakonczyles dzialanie programu. \n");
            return 0;
        }
        }
    }
    return 0;
}
