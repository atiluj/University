#include <stdlib.h>  //lista 2 zad. 2
#include <stdio.h>
#include <stdbool.h>

void wypisz_stos(int dl, int stos[])
{
    printf("stos:(");
    for(int i = 0; i < dl; i++)
    {
        printf("%d,", stos[i]);
    }
    printf(") \n");
}

int main()
{
    int dl;
    scanf("%d", &dl);
    //printf("dlugosc: %d \n", &dl);
    int stos[dl];
    int arg1, arg2, znak;
    int wierzcholek = 0;
    getchar();
    char pom[dl];
    for(int i = 0; i < dl; i++)
    {
        pom[i] = getchar();
    }
    char wyrazenie[dl];
    int k = dl - 1;
    for(int i = 0; i < dl; i++)
    {
        wyrazenie[i] = pom[k];
        k--;
    }

    for(int i = 0; i < dl; i++)
    {
        if(wyrazenie[i] >= '0' && wyrazenie[i] <= '9')
        {
            znak = (int)(wyrazenie[i] - 48);
            stos[wierzcholek] = znak;
            wierzcholek++;
        }
        else
        {
            arg1 = stos[wierzcholek - 1];
            arg2 = stos[wierzcholek - 2];
            wierzcholek = wierzcholek - 2;
            switch(wyrazenie[i])
            {
            case '-':
                stos[wierzcholek] = arg1 - arg2;
                wierzcholek++;
                if(i == dl - 1)
                {
                    printf("%d", stos[0]);
                    return 0;
                }
                break;
            case '+':
                stos[wierzcholek] = arg1 + arg2;
                wierzcholek++;
                if(i == dl - 1)
                {
                    printf("%d", stos[0]);
                    return 0;
                }
                break;
            case '*':
                stos[wierzcholek] = arg1 * arg2;
                wierzcholek++;
                if(i == dl - 1)
                {
                    printf("%d", stos[0]);
                    return 0;
                }
                break;
            }
        }
    }
    return 0;
}
