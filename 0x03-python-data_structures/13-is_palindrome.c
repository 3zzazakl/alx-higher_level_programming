#include "lists.h"

/**
 * is_palindrome - check if linked list is palindrome
 * @head: pointer to pointer
 * Return: (1) if palindrome, otherwise (0)
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *f_half = *head;
	listint_t *s_half;
	listint_t *prev = NULL;
	listint_t *cur, *next;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	cur = slow;

	while (cur)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	s_half = prev;


	while (s_half)
	{
		if (f_half->n != s_half->n)
			return (0);

		f_half = f_half->next;
		s_half = s_half->next;
	}

	return (1);
}
