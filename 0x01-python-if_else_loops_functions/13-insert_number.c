#include "lists.h"
/**
 * insert_node - Inserts number into sorted singly-linked list.
 * @head: A pointer that points head of the linked list.
 * @number: number to be insert.
 * Return: function fails - NULL.
 *         Otherwise - a pointer to new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
