#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to check
 * Return: 1 if cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_list, *slow_list;

	if(!list || !list->next)
	{
		return(0);
	}
	fast_list = list;
	slow_list = list;

	while(fast_list != NULL && slow_list != NULL && fast_list->next != NULL)
	{
		fast_list = fast_list->next->next;
		slow_list = slow_list->next;
		if(slow_list == fast_list)
		{
			return(1);
		}
	}
	return(0);
}
