#include "bst.h"
//lista 4 zadanie 1
Node* new_node(int x){
        Node* nowy = (Node*)malloc(sizeof(Node));
        nowy->value = x; //.
        nowy->left = NULL; //.
        nowy->right = NULL; //.
        return nowy; }

Node* dodawanie(Node* drzewo, int x)
{
    Node* nowy = new_node(x);
    nowy->value = x;

    if(drzewo == NULL)
    {
        return nowy;
    }

    Node* n = drzewo;
    Node* rodzic = NULL;

    while(n != NULL)
    {
        rodzic = n;
        if(x >= n->value)
            n = n->right;
        else n = n->left;
    }
    if(rodzic->value >= x)
        rodzic->left = nowy;
    else rodzic->right = nowy;
    return drzewo;
}

Node* usuwanie(Node* drzewo, int x) ///nie mozemy usuwc z pustej tablicy
{
    if(drzewo == NULL)
    {
        printf("Nie odejme od pustego drzewa");
        return 0;
    }
    if(drzewo->value > x)
        usuwanie(drzewo->left, x);
    if(drzewo->value < x)
    {
        usuwanie(drzewo->right, x);
    }
    else // gdy drzewo->value == x
    {
        //printf("Usuwam element: %d \n", x);
        Node* lewa = drzewo->left;
        Node* prawa = drzewo->right;
        if(lewa == NULL)
        {
            printf("lewa = NULL \n");
            free(drzewo);
            printf("\n");
            drzewo = prawa;
            posortuj(drzewo);
            return drzewo;
        }
        free(drzewo);
        drzewo = lewa;
        while(lewa->right != NULL)
        {
            lewa = lewa->right;
        }
        lewa->right = prawa;
    }
    return drzewo;
}

bool wyszukanie(Node* drzewo, int x)
{
    if(drzewo == NULL) //przypadek gdy drzewo puste
        return 0;
    if(x == drzewo->value)
        return 1;
    if(x < drzewo->value)
        return wyszukanie(drzewo->left, x);
    return wyszukanie(drzewo->right, x);
}

int wysokosc(Node* drzewo)
{
    if(drzewo != NULL)
    {
        if(wysokosc(drzewo->left) > wysokosc(drzewo->right))
            return 1 + wysokosc(drzewo->left);
        else return 1 + wysokosc(drzewo->right);
    }
    else return 0;
}

void posortuj(Node* drzewo)
{
    if(drzewo != NULL)
    {
        posortuj(drzewo->left);
        printf("%d, ", drzewo->value);
        posortuj(drzewo->right);
    }
}
