#include "lists.h"
/**
 * check_cycle - check if a list is a cycle or not
 * @list: struct
 * Return: 1 if is a cyrcle or 0
 */
int check_cycle(listint_t *list)
{
	listint_t **tempmem = NULL;
	listint_t *temp = NULL, *temp2 = NULL;

	temp = list;
	tempmem = &list;

	if (list == NULL)
		return (0);
	if (temp->next)
		if (temp->next)
			temp2 = temp->next->next;

	while (temp2 != NULL)
	{
		temp = temp->next;
		if (temp == *(tempmem) || temp == temp2)
			return (1);
		/* temp = temp->next; */
		temp2 = temp2->next;
	}
	return (0);
}
