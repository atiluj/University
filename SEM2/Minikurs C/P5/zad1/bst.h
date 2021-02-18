#include <stdio.h>   // lista 4 zadanie 1
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

typedef struct node {
int value; //wartosc
struct node* left; //lewe poddrzewo
struct node* right; // prawe poddrzewo
}Node;


Node* dodawanie(Node* drzewo, int x);
Node* usuwanie(Node* drzewo, int x);
bool wyszukanie(Node* drzewo, int x);

int wysokosc(Node* drzewo);
void posortuj(Node* drzewo);
