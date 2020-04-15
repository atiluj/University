#include <assert.h> //lista 5 zad 2
#include <stdlib.h>
#include <string.h>
#include "fifo.h"

struct node
{
    int data_type; //typ zmiennej
    size_t allocated_size;
    void *data;
    struct node *next_node;
};

typedef struct node node_t;

void init(struct fifo *fifo) //pusta kolejka
{
    fifo->head = NULL;
    fifo->tail = NULL;
}

void clear(struct fifo *fifo) //wyczyszczeni całej kolejki
{
    node_t *node = fifo->head;
    while(node != NULL) //przechodze po calej kolejce
    {
        node_t *tmp_node = node; //usuwam
        node = node->next_node;
        free(tmp_node);
    }
    fifo->head = NULL;
    fifo->tail = NULL;
}

int pop(struct fifo *fifo, int *data_type, size_t *allocated_size, void *data)
{
    node_t *head = fifo->head;
    if (NULL == head) //z pustej kolejki nie da się usunąc elementu
        return -1;

    node_t *next = head->next_node;

    if (next == NULL) //gdy kolejka miała tylko jeden elment
        fifo->tail = NULL;
    fifo->head = next;

    *data_type = head->data_type;
    *allocated_size = head->allocated_size;
    //void *memcpy (void* dest, const void* src, size_t size);
    //Funkcja kopiuje size bajtów z obiektu source do obiektu dest.
    memcpy(data, head->data, *allocated_size);
}
