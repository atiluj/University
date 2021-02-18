//lista 5 zad 2
#ifndef __FIFO_H__ //#if !defined
#define __FIFO_H__
#include <stddef.h>

struct node;

struct fifo
{
  struct node *head;
  struct node *tail;
};

void init(struct fifo *fifo); //inicjalizacja pustej kolejki
void clear(struct fifo *fifo); //czyści kolejkę

//int push(struct fifo *fifo, int data_type, size_t allocated_size, void *data);
int pop(struct fifo *fifo, int *data_type, size_t *allocated_size, void *data);

#endif //koniec bloku kompilacji warunkowej
