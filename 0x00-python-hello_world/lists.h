#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(cons listint_t *h);
listint_t *add_nodeint(listint_t **head, cons int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
