#include "lists.h"

/**
 * is_palindrome - check if linked list is palindrome
 * @head: pointer to pointer
 * Return: (1) if palindrome, otherwise (0)
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = NULL;
	listint_t *fast = NULL;
	int len = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	slow = fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		len++;
	}

	if ((*head) != NULL)
	{
		for (len /= 2, slow = *head; len > 0; --len, slow = slow->next)
		;
	}

	return ((*head)->n != slow->n);
}
