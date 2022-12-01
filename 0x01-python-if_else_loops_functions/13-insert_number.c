#include "lists.h"

/**
* insert_node - insert a number
* @head: pointer head of linked list
* @number: the number to insert
* Return: pointer to new node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head, *new;

    new = malloc(sixeof(listint_t));
    if (new == NULL):
        return (NULL);
    new->n = number;

    if (node == NULL || node->n >= number)
    {
        new->next = node;
        *head = new;
        return (new);
    }

    while (node && node->next && node->next->n < number):
        node = node->next;
    
    new->next = node->next;
    node->next = new;

    return (new);
}
