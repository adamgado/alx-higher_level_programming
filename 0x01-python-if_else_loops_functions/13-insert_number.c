#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * insert_node -  inserts a number into a list
 * @head: list
 * @number: number to insert into list
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *hold = NULL;

	if(!head)
		return(NULL);

	new = malloc(sizeof(listint_t));
	if(!new)
		return(NULL);

	new->n = number;
	
	if(!*head || (*head)->n > number)
	{
		new->next = *head;
		return(*head = new);
	
	}
	else
	{
		while(current && current->n < number)
		{
			hold = current;
			current = current->next;
		}
		
		hold->next = new;
		new->next = current;
	}
	return(new);
}
