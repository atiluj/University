#include "bst.h"
#include <stdlib.h>
#include <time.h>
// Julita Osman 314323 lista 4 zadanie 1
int main()
{
    Node* drzewo = NULL;
    srand(time(0));
    printf("Dodanie 106 losowych liczb do drzewa bst z przedzialu 1-300. \n");
    for(int i = 0; i < 106; i++)
    {
        drzewo = dodawanie(drzewo, rand()%301);
    }
    printf("\nWysokosc drzewa: %d \n", wysokosc(drzewo));
    printf("Posortowane drzewo: ");
    posortuj(drzewo);

    //sprzawdzenie czy dane liczby znajdj¹ siê w naszym drzewiw
    /*assert(wyszukanie(drzewo, 11) == 1);
    * assert(wyszukanie(drzewo, 100) == 1);
    * assert(wyszukanie(drzewo, 3) == 1);
    * assert(wyszukanie(drzewo, 25) == 1);
    * assert(wyszukanie(drzewo, 8) == 1); */

    //usuniecie elementu
    printf("\n");
    printf("\nDrzewo po usunieciu elementu o wartosci: %d \n", drzewo->value);
    drzewo = usuwanie(drzewo, drzewo->value);
    posortuj(drzewo);

    return 0;

}
