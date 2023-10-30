#include "lists.h"
/**
 * check_cycle - check if linked list has a cycle
 * @list: pointer to head of list.
 * Return: (0) if no cycle otherwise (1) if has a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
