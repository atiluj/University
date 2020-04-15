#include <stdlib.h>  //lista 2 zad. 2
#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

#define MODULUS 100000000  //do podpunktu b

struct mem_entry {   // do podpunkt c
    unsigned long value;
    bool valid;
};

struct mem_entry memory[MODULUS]; //tablica zadeklarowana globalnie

//podpunkt a
unsigned long catalan(unsigned short n)
{
    if(n <= 1)
        return 1;

    long int wynik = 0;
    for(int i = 0; i < n; i++)
    {
        wynik = wynik + catalan(i) * catalan(n - i - 1);
    }
    return wynik;
}

//podpunkt b
unsigned long catalan_M(unsigned short n)
{
    if(n <= 1)
        return 1;

    long int wynik = 0;
    for(int i = 0; i < n; i++)
    {
        wynik = wynik + catalan_M(i) * catalan_M(n - i - 1);
    }
    return wynik%MODULUS;
}

//podpunkt c
unsigned long catalanMem(unsigned short n)
{
    if(memory[n].valid == true)
        return memory[n].value;

    if(n <= 1)
    {
        memory[n].value = 1;
        memory[n].valid = true;
        return 1;
    }

    long int wynik = 0;
    for(int i = 0; i < n; i++)
    {
        memory[i].value = catalanMem(i);
        memory[i].valid = true;
        memory[n - i - 1].value = catalanMem(n - i - 1);
        memory[n - i - 1].valid = true;
        wynik = wynik + memory[i].value * memory[n - i - 1].value;
    }
    return wynik%MODULUS;
}


int main(){
    /*int wynik, wynik_M, wynikMem;
    wynik = catalan(6); //numer liczby Catalana
    wynik_M = catalan_M(5);
    wynikMem = catalanMem(4);
    printf("Podpunkt a (szosta liczba): \n");
    printf("%li \n", wynik);
    printf("Podpunkt b: (piata liczba) \n");
    printf("%li \n", wynik_M);
    printf("Podpunkt c: (czwarta liczba) \n");
    printf("%li \n", wynikMem);*/


    assert(catalan(0) == 1);
    assert(catalan(1) == 1);
    assert(catalan(2) == 2);
    assert(catalan(3) == 5);
    assert(catalan(4) == 14);
    assert(catalan_M(1) == 1);
    assert(catalan_M(2) == 2);
    assert(catalan_M(3) == 5);
    assert(catalan_M(5) == 42);
    assert(catalan_M(6) == 132);
    assert(catalanMem(1) == 1);
    assert(catalanMem(0) == 1);
    assert(catalanMem(4) == 14);
    assert(catalanMem(5) == 42);
    assert(catalanMem(6) == 132);

    return 0;
}
