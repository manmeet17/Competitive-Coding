#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *next;
}*head;
void create_list(struct node *head,int n);
void display(struct node *head,int n);
main()
{
	head=(struct node *)malloc(sizeof(struct node *));
	create_list(head,5);
}
void create_list(struct node *head,int n)
{
	struct node *temp,*n1;
	int i;
	n1=(struct node *)malloc(sizeof(struct node *));
	printf("Enter number\n");
	scanf("%d",&n1->data);
	n1->next=NULL;
	head=n1;
	for (i=0;i<n;i++)
	{
		temp=(struct node *)malloc(sizeof(struct node *));
		printf("Enter number\n");
		scanf("%d",&temp->data);
		temp->next=NULL;
		n1->next=temp;
		printf("%d",n1->data);
		n1=temp;
		
	}
	printf("List created\n");
}
