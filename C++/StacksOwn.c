#include<stdio.h>
void push();
void pop();
void display();
int n=5,top,x;
int stack[5];
void main()
{
    int choice,option=1;
    top =-1;
    while(option)
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
        	printf("Enter element:");
        	scanf("%d",&x);
            push(x);
            break;
        case 2:
            pop();
            break;
        case 3:
        	display();
        	break;
        default:
        	option=0;
        }
    }
}
void push(x)
{
	if(top>=n-1)
	printf("Overflow\n");
	else
	{
		top++;
		stack[top]=x;
	}
}
void pop()
{
	if(top<=-1)
	printf("Underflow\n");
	else
	printf("Popper element is :%d \n",stack[top]);
	top--;
	
}
void display()
{
	int i;
	for(i=0;i<=top;i++)
	printf("%d\n",stack[i]);
}
