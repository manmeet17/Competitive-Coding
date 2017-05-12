#include <stdio.h>
struct stack
{
    int stk[5];
    int top;
};
typedef struct stack STACK;
STACK s;
 
void push(void);
int  pop(void);
void display(void);
 
void main ()
{
    int choice;
    int option = 1;
    s.top = -1;
 
    while (option)
    {
        printf("1 -->PUSH \n");
        printf("2 -->POP \n");
        printf("3 --> Display The Stack\n");
        printf("Enter your choice\n");
        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
            push();
            break;
        case 2:
            pop();
            break;
        case 3:
        	display();
        	break;
        }
    }
}
/*  Function to add an element to the stack */
void push ()
{
    int num;
    if (s.top == (4))
    {
        printf ("Overflow\n");
        return;
    }
    else
    {
        printf ("Enter the element to be pushed\n");
        scanf ("%d", &num);
        s.top = s.top + 1;
        s.stk[s.top] = num;
    }
    return;
}
/*  Function to delete an element from the stack */
int pop ()
{
    int num;
    if (s.top == - 1)
    {
        printf ("Underflow\n");
        return (s.top);
    }
    else
    {
        num = s.stk[s.top];
        printf ("Poped element is = %d\n", s.stk[s.top]);
        s.top = s.top - 1;
    }
}
/* Function to display the stack */
void display()
{
	int i;
	for(i=0;i<=s.top;i++)
	printf("%d \n",s.stk[i]);
	return;
}
