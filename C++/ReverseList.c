#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *next;
}*head;
void *create_list(struct node *head,int n);
void *reverse(struct node *head,int n);
void display(struct node *head,int n);
main()
{
	head=(struct node *)malloc(sizeof(struct node *));
	head=create_list(head,5);
	reverse(head,5);
}
void *create_list(struct node *head,int n)
{
	struct node *temp,*n1;
	int i;
	n1=(struct node *)malloc(sizeof(struct node *));
	printf("Enter number\n");
	scanf("%d",&n1->data);
	n1->next=NULL;
	head=n1;
	for (i=0;i<n-1;i++)
	{
		temp=(struct node *)malloc(sizeof(struct node *));
		printf("Enter number\n");
		scanf("%d",&temp->data);
		temp->next=NULL;
		n1->next=temp;
		n1=temp;
	}
	printf("List created\n");
return head;
}
void display(struct node *head,int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		printf("%d-",head->data);
		head=head->next;
	}
}
void *reverse(struct node *head,int n)
{
	int i=1;
	struct node *n1=head;
	while(i<n)
	{
		n1=n1->next;
		i++;
	}
	for(i=1;i<=n;i++)
	{
		printf("%d\n",n1->data);
		n1=&n1->data;
	}	
}
