#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Insert node in sorted singly linked list
 * @head: pointer to head of list
 * @number: number to insert in linked list
 * Return: address of the new node or null if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *nextnode;

	current = *head;
	nextnode = current->next;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	/*new->next = NULL;*/
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->n < number && number < nextnode->n)
			{
				current->next = new;
				new->next = nextnode;
				return (new);
			}
			current = current->next;
			nextnode = current->next;
		}
		current->next = new;
		new->next = NULL;
	}
	return (new);
}
