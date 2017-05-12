#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *prev;
	struct node *next;
};
main()
{
	int i;
	struct node *head=(struct node *)malloc(sizeof(struct node *));
	struct node *n=head;
	struct node *n1=head;
	struct node *p=head;
	printf("Enter the data in head:");
	scanf("%d",&head->data);
	head->prev=NULL;
	head->next=NULL;
	for(i=1;i<5;i++)
	{
		struct node *temp=(struct node *)malloc(sizeof(struct node *));
		printf("Enter data:");
		scanf("%d",&temp->data);
		temp->prev=head;
		head->next=temp;
		temp->next=NULL;
		head=temp;
	}
	printf("List created\n");
		while(n!=NULL)
		{
			printf("%d\n",n->data);
			n=n->next;
		}
	printf("Reverse:\n");
	for(i=1;i<=5;i++)
	{
		while(head!=NULL)
		{
			printf("%d\n",head->data);
			head=head->prev;
		}
	}
	int loc;
	i=1;
	struct node *k=(struct node *)malloc(sizeof(struct node *));
	printf("Enter data for insertion");
	scanf("%d",&k->data);
	printf("Where do u want to insert the node:");
	scanf("%d",&loc);
	while(i<loc)
	{
		n1=n1->next;
		i++;
	}
	n1->prev->next=k;
	k->next=n1;
	k->prev=n1->prev;
	n1->prev=k;
		while(p!=NULL)
		{       
			printf("%d\n",p->data);
			p=p->next;
		}
}

