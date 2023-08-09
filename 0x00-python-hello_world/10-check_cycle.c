#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *x;
	listint_t *y;

	x = list;
	y = list;
	while (list && x && x->next)
	{
		list = list->next;
		x = x->next->next;

		if (list == x)
		{
			list = y;
			y =  x;
			while (1)
			{
				x = y;
				while (x->next != list && x->next != y)
				{
					x = x->next;
				}
				if (x->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}