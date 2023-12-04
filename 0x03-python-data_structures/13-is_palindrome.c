#include "lists.h"
/**
 * reverse_list - Reverse linked list
 * @head: pointer to starting node of a list
 * Return: pointer to head of reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = *head, *next, *prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}
/**
 * is_palindrome - Check if list is a palindrome
 * @head: pointer to head of a list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	listint_t *reversed;
	size_t size = 0;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	if ((size % 2) == 0 && temp->n != temp->next->n)
	{
		return (0);
	}
	temp = *head;
	reversed = reverse_list(&temp);
	while (reversed != NULL)
	{
		if (temp->n != reversed->n)
			return (0);
		temp = temp->next;
		reversed = reversed->next;
	}

	return (1);
}
