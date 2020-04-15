#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
//pracownia 4 zadanie 2

#define DEFAULT_SIZE 2

struct vector
{
    int size; // ile mamy elementow
    int capacity; // ile mo¿emy mieæ elementow
    int *data; // wskaznik na dane
};

typedef struct vector vector_t;

int czytaj(vector_t *v, int i)
{
    assert(v->size > i); //warunek na to aby i nie wyszlo poza rozmiar
    return v->data[i];
}

void usun_z_konca(vector_t *v)
{
    assert(v->size >= 1); //sprawdzamy czy nie usuwamy z konca pustego wektora
    v->size--;
}

void dodaj_na_koniec(vector_t *v, int x)
{
    if (v->capacity > v->size) //przypadek 1) gdy mamy wystarczajaco miejsca
    {
        v->data[v->size] = x;
        v->size++;
        return;
    }
    //przypadek 2) gdy mamy za malo miejsca
    if (v->capacity == 0) //podprzypadek 1) gdy pojemnosc tablicy jest równy 0, stworzymy więc domyslny rozmiar
    {
        assert(v->size == 0); //sprawdzamy rozmiar, w przypadku gdy pojemnosc = 0 rozmiar powinien byc rowny 0
        v->capacity = DEFAULT_SIZE;
        v->data = malloc(sizeof(int) * v->capacity); // alokujemy pamiec
        assert(v->data != NULL);
        v->data[v->size] = x; //dodajemy
        v->size++; //zwiekszamy rozmiar
    }
    else //podprzypadek 2) stworzenie nowej dwa razy wiekszej tablicy
    {
        int capacity = v->capacity * 2; //zwiekszenie pojemnosci
        int *data = malloc(sizeof(int) * capacity); // nowa tablica
        assert(data != NULL);

        for (int i = 0; i < v->capacity; ++i) //przepisujemy stara tablice
        {
            data[i] = v->data[i];
        }

        free(v->data); //zwalniamy stara pamiec
        v->data = data;
        v->capacity = capacity;
        v->data[v->size] = x;
        v->size++;
    }
}

vector_t *stworz_vector(void)
{
    vector_t *vector = malloc(sizeof(vector_t));
    vector->size = 0;
    vector->capacity = DEFAULT_SIZE;
    vector->data = malloc(sizeof(int) * vector->capacity); //stowrzenie tablicy rozmiaru pojemnosci
    assert(vector->data != NULL);
    return vector;
}

void zwolnij_vector(vector_t *v)
{
    v->size = 0; //ustawiamy rozmiar na 0, ale nie zwalniamy pamieci

    /* opcja 2 ze zwolnieniem pamieci
    assert(v->capacity > 0);
    v->size = 0;
    v->capacity = 0;
    free(v->data);
    v->data = NULL; */
}


int main(void)
{
    printf("Dodaje do tablic 10 elementow. \n");
    vector_t *v = stworz_vector();
    //usun_z_konca(v);
    for (int i = 0; i < 10; ++i)
        dodaj_na_koniec(v, i);
    printf("Wypisuje 11 elementow tablicy. Tablica nie ma elementu jedenastego wiec powinna zwrocic blad. \n");
    for (int i = 0; i < 11; ++i)
    {
        printf("Element %d: ", i+1);
        printf("%d\n", czytaj(v, i));
    }

    return 0;
}


