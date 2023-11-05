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
	listint_t *f_half = NULL;
	listint_t *s_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	slow = fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	f_half = *head;
	s_half = slow;

	while (s_half)
	{
		if (f_half->n != s_half->n)
			return (0);

		f_half = f_half->next;
		s_half = s_half->next;
	}

	return (1);
}
