#include "lists.h"
#include <stdio.h>

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/** 
 * reverse_listint - Reverses a singly linked list
 * @head: a pointer to the starting node of the list
 *
 * Return: a pointer to the ending node of the list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while(node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the starting node of the list
 *
 * Return: 0 if palindrome
 * 	   1 if not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev, *tmp;

	if (*head == NULL || (*head)->next == NULL)
			return (1);

	tmp = *head;
	rev = reverse_listint(&tmp);

	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);

		tmp = tmp->next;
		rev = rev->next;
	}

	return (1);
}
