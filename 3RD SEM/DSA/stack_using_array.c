/* 22/09/26
 Stack implementation using an array 
*/

#include <stdio.h>
#define MAX 5
int stack[MAX];
int top = -1;
void push(void)
{
	int value;
	if (top == MAX - 1) {
		printf("Stack Overflow\n");
		return;
	}
	printf("Enter value to push: ");
	scanf("%d", &value);
	stack[++top] = value;
	printf("%d pushed into the stack\n", value);
}
void pop(void)
{
	if (top == -1) {
		printf("Stack Underflow\n");
		return;
	}
	printf("%d popped from the stack\n", stack[top--]);
}
void peek(void)
{
	if (top == -1) {
		printf("Stack is empty\n");
		return;
	}
	printf("Top element: %d\n", stack[top]);
}
void display(void)
{
	int index;
	if (top == -1) {
		printf("Stack is empty\n");
		return;
	}
	printf("Stack elements (top to bottom):\n");
	for (index = top; index >= 0; index--) {
		printf("%d\n", stack[index]);
	}
}
int main(void)
{
	int choice;

	do {
		printf("\n--- Stack Using Array ---\n");
		printf("1. Push\n");
		printf("2. Pop\n");
		printf("3. Peek\n");
		printf("4. Display\n");
		printf("5. Exit\n");
		printf("Enter your choice: ");
		scanf("%d", &choice);
		switch (choice) {
		case 1:
			push();
			break;
		case 2:
			pop();
			break;
		case 3:
			peek();
			break;
		case 4:
			display();
			break;
		case 5:
			printf("Exiting...\n");
			break;
		default:
			printf("Invalid choice\n");
		}
	} while (choice != 5);
	return 0;
}
