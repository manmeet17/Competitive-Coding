#include <stdio.h>
struct stack
{
    int arr[5];
    int top;
};
struct stack s;
 
void push();
int  pop();
void display();
void main()
{
    int choice,option=1;
    s.top = -1;
    while (option==1)
    {
        printf("1-Push \n");
        printf("2-Pop \n");
        printf("3-Display The Stack\n");
        printf("4-Quit \n");
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
        case 4:
        	option=2;
        }
    }
}
void push()
{
    int num;
    if (s.top==(4))
    {
        printf ("Overflow\n");
        return;
    }
    else
    {
        printf ("Enter the element to be pushed\n");
        scanf ("%d",&num);
        s.top++;
        s.arr[s.top]=num;
    }
    return;
}
int pop ()
{
    int num;
    if (s.top==-1)
    {
        printf("Underflow\n");
        return(s.top);
    }
    else
    {
        num=s.arr[s.top];
        printf("Poped element is = %d\n",s.arr[s.top]);
        s.top--;
    }
}
void display()
{
	int i;
	printf("The current stack is:\n");
	for(i=0;i<=s.top;i++)
	printf("%d \n",s.arr[i]);
	return;
}
