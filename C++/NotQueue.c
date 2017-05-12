#include <stdio.h>
struct queue
{
int arr[5];
int rear;
int front;
};
struct queue s;

void enqueue();
int dequeue();
void display();

void enqueue()
{
    int num;
    if (s.rear==4)
    printf("Overflow \n");
    else
    {
        if(s.front==-1)
        s.front=0;
        printf("Inset the element in queue : ");
        scanf("%d",&num);
        s.rear++;
        s.arr[s.rear]=num;
    }
} 
int dequeue()
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
    return;
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
main()
{
    int choice=1;
    s.front=-1,s.rear=-1;
    while(choice==1)
    {
        printf("1.Insert \n");
        printf("2.Delete \n");
        printf("3.Display elements of the queue \n");
        printf("4.Quit \n");
        printf("Enter your choice :");
        scanf("%d",&choice);
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
            	choice=0;
            	break;
        } 
   }
}

