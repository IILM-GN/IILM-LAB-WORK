/* Implement all the operations of stack in c programming language : push , poop , IsEmpty(underflow) , IsSize , IsFull (Overflow).
Size of stack = 10 
    push - 5
    pop - 2
    push - 3
*/

#include <stdio.h>
#include <stdlib.h>

#define STACK_SIZE 10

typedef struct {
    int items[STACK_SIZE];
    int top;
} Stack;

void initStack(Stack *s) {
    s->top = -1;
}

int isEmpty(Stack *s) {
    return s->top == -1;
}

int isFull(Stack *s) {
    return s->top == STACK_SIZE - 1;
}

int getSize(Stack *s) {
    return s->top + 1;
}

void push(Stack *s, int value) {
    if (isFull(s)) {
        printf("Overflow! Cannot push %d. Stack is full.\n", value);
        return;
    }
    s->items[++(s->top)] = value;
    printf("Pushed %d onto the stack.\n", value);
}

int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Underflow! Cannot pop. Stack is empty.\n");
        return -1;
    }
    return s->items[(s->top)--];
}

void printStack(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty.\n");
        return;
    }
    printf("Current Stack Contents (Top -> Bottom): ");
    for (int i = s->top; i >= 0; i--) {
        printf("%d ", s->items[i]);
    }
    printf("\n");
}

int main() {
    Stack myStack;
    initStack(&myStack);
    int value, count, choice;

    printf("--- Initial Stack Setup ---\n");
    printf("Enter the number of integers to initialize the stack (max %d): ", STACK_SIZE);
    scanf("%d", &count);

    if (count < 0 || count > STACK_SIZE) {
        printf("Invalid count. Setting to 0.\n");
        count = 0;
    }

    printf("Enter %d integer(s):\n", count);
    for (int i = 0; i < count; i++) {
        printf("Value %d: ", i + 1);
        scanf("%d", &value);
        // Directly assign to simulate initial stack fill
        if (!isFull(&myStack)) {
            myStack.items[++(myStack.top)] = value;
        } else {
            printf("Warning: Stack limit reached. Value %d ignored.\n", value);
            break;
        }
    }

    printf("\nInitial Stack Loaded. Size: %d\n", getSize(&myStack));
    printStack(&myStack);

    while (1) {
        printf("\n--- Stack Menu ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Is Empty\n");
        printf("4. Is Full\n");
        printf("5. Get Size\n");
        printf("6. Print Stack\n");
        printf("7. Exit\n");
        printf("Enter choice: ");
        
        if (scanf("%d", &choice) != 1) {
            while(getchar() != '\n'); 
            printf("Invalid input. Please enter a number.\n");
            continue;
        }

        switch (choice) {
            case 1:
                if (isFull(&myStack)) {
                    printf("Cannot push: Stack is full (Overflow).\n");
                } else {
                    printf("Enter value to push: ");
                    scanf("%d", &value);
                    push(&myStack, value);
                }
                break;
            case 2:
                if (isEmpty(&myStack)) {
                    printf("Cannot pop: Stack is empty (Underflow).\n");
                } else {
                    value = pop(&myStack);
                    printf("Popped value: %d\n", value);
                }
                break;
            case 3:
                printf("Is Empty? %s\n", isEmpty(&myStack) ? "Yes" : "No");
                break;
            case 4:
                printf("Is Full? %s\n", isFull(&myStack) ? "Yes" : "No");
                break;
            case 5:
                printf("Current Size: %d\n", getSize(&myStack));
                break;
            case 6:
                printStack(&myStack);
                break;
            case 7:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice. Try again.\n");
        }
    }
    return 0;
}

/*
FUNCTION DEFINITIONS:
- initStack: Initializes the stack by setting 'top' to -1 (empty state).
- isEmpty: Returns true if 'top' is -1; used to detect Underflow before popping.
- isFull: Returns true if 'top' equals STACK_SIZE - 1; used to detect Overflow before pushing.
- getSize: Returns the current number of elements stored (calculated as top + 1).
- push: Adds a new element to the top of the stack if space is available.
- pop: Removes and returns the top element if the stack is not empty.
- printStack: Iterates from 'top' down to 0 to display current contents.
*/