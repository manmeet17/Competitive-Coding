#include <stdio.h>
struct queue
{
int arr[5];
int rear;
int front;
};
struct queue s,s1;

void enqueue();
void dequeue();
void display();
void reverse();

main()
{
    int choice=1;
    s.front=-1,s.rear=-1;
    while (choice!=0)
    {
        printf("1.Insert \n");
        printf("2.Delete \n");
        printf("3.Display elements of the queue \n");
        printf("4.Reverse the queue \n");
        printf("5.Quit \n");
        printf("Enter your choice : ");
        scanf("%d", &choice);
        switch (choice)
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
            	reverse();
            	break;
            case 5:
            	choice=0;

        }
   }
}
void enqueue()
{
    int num;
    if (s.rear==4)
    printf("Queue Overflow \n");
    else
    {
        if(s.front==-1)
        s.front = 0;
        printf("Inset the element in queue : ");
        scanf("%d",&num);
        s.rear++;
        s.arr[s.rear]=num;
    }
}
void revenqueue(int x)
{
	if(s1.front=-1)
	{
		s1.front=0;
	}
	s1.rear++;
	s1.arr[s1.rear]=x;
}
void dequeue()
{
    if(s.front==-1 || s.front>s.rear)
    {
        printf("Underflow \n");
        return;
    }
    else
    {
        printf("Element deleted from queue is : %d\n",s.arr[s.front]);
        s.front++;
    }
} 
void redequeue()
{
    if(s1.front==-1 || s1.front>s1.rear)
    {
        printf("Underflow \n");
        return;
    }
    else
    {
        printf("Element deleted from queue is : %d\n",s1.arr[s1.front]);
        s1.front++;
    }
}
void display()
{
    int i;
    if (s.front==-1)
        printf("Queue is empty \n");
    else
    {
        printf("Queue is: \n");
        for(i=s.front;i<=s.rear;i++)
            printf("%d \n",s.arr[i]);
    }

}
void reverse()
{
	int i;
	s1.front=-1;
	s1.rear=-1;
	for(i=s.rear;i>=s.front;i--)
	{
		revenqueue(s.arr[i]);
	}
	for(i=s1.front;i<=s1.rear;i++)
	{
		printf("%d\n",s1.arr[i]);
	}
}
