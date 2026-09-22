//08/09/2026
//Singly Linked List Implementation

#include <stdio.h>
#include <stdlib.h>
struct node{
    int data;
    struct node *next;

};
int main () {
struct node *head, *new, *temp;
    head = malloc(sizeof(struct node));
    new = malloc(sizeof(struct node));

    printf("Enter 1st value :");
    scanf("%d", &head->data);

    printf("Enter 2nd value :");
    scanf("%d", &new->data);

    head->next = new;
    new->next = NULL;

    temp = head;
    printf("\n LINKED LIST: ");
        while(temp != NULL){
            printf("%d ", temp->data);
            temp = temp->next;
    }

printf("NULL\n");
free(head);
free(new);
return 0;

}
