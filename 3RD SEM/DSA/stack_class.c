#include <stdio.h>

#define MAX 5
int stack[MAX];
int top = -1;

void push()
{
    int value;
    if (top == MAX - 1)
    {
        printf("Stack Overflow\n");
    }
    else
    {
        printf("Enter value to push: ");
        scanf("%d", &value);
        top++;
        stack[top] = value;
        printf("%d pushed into stack\n", value);
    }

}
void pop()
{
    if (top == -1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        printf("%d popped from stack\n", stack[top]);
        top--;
    }
}
int main()
{
    int n, i;
    printf("How many elements do you want to push? ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        push();
    }
    printf("\nPerforming Pop operation:\n");
    pop();
    pop();
    return 0;
}