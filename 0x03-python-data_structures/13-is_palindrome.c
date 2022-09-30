#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

#define false 1

void reverse_list(listint_t **head);

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to the start of the list
 *
 * Return: 0 if not palindrome, 1 if it is.
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *slow = *head, *cp =  NULL, *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (false)
	{
		fast = fast->next->next;
		if (!fast)
		{
			cp = slow->next;
			break;
		}
		if (!fast->next)
		{
			cp = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_list(&cp);

	while (cp && temp)
	{
		if (temp->n == cp->n)
		{
			cp = cp->next;
			temp = temp->next;
		}

		else
			return (0);
	}
	
	if (!cp)
		return (1);
	return (0);
}

/**
 * reverse_list - reverses a listint_t
 * @head: pointer to the list
 *
 * Return: pointer to the reversed list
 */

void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;
	listint_t *current = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	
	*head = prev;

}
