#include "lists.h"

/**
 * check_cycle - checks linked list cycle
 * @list: linked liss
 *
 * Return: return 1 if the list has a cycle, return 0 if it has not
 */
int check_cycle(listint_t *list)
{
	listint_t *higher = list;
	listint_t *lower = list;

	if (!list)
		return (0);

	while (higher && lower && lower->next)
	{
		higher = higher->next;
		lower = lower->next->next;
		if (higher == lower)
			return (1);
	}

	return (0);
}
