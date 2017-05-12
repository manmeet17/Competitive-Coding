#include<stdio.h>
struct queue
{
	int arr[5];
	int head;
	int tail;
};
struct queue s;
void enqueue()
{
	int num;
	if(s.head==-1 && s.tail==-1)
	{
		s.head=0;
		s.tail=0;
	}
	if(s.tail==5)
	{
		printf("Overflow \n");
		return;
	}
	else
	{
		printf("Enter element to be added:\n");
		scanf("%d",&num);
		s.arr[s.tail]=num;
		s.tail++;
	}
	return;
}
void dequeue()
{
	if(s.head<0 || s.head>=s.tail)
	{
	printf("Underflow \n");
	return;
	}
	else
	{
		printf("Element removed is:%d \n",s.arr[s.head]);
		s.head++;
		s.tail--;
	}
	return;
}
void display()
{
	int i;
	for(i=s.head;i<=s.tail;i++)
	printf("%d \n",s.arr[i]);	
}
main()
{
	s.head=-1;
	s.tail=-1;
	int choice,opt=1;
	 while (opt==1)
    {
        printf("1-Enqueue \n");
        printf("2-Dequeue \n");
        printf("3-Display The Queue\n");
        printf("4-Quit \n");
        printf("Enter your choice\n");
        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
            enqueue();
            break;
        case 2:
            dequeue();
            break;
        case 3:
        	display();
        	break;
        case 4:
        	opt=2;
    	}
	}
}
