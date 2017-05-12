#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *next;
}*head;
struct node *create_list(struct node *head,int n);
void display(struct node *head);
void *addbegin(struct node *head);
void *addmiddle(struct node *head);
void *addend(struct node *head,int n);
void *delbegin(struct node *head);
void *delmiddle(struct node *head,int n);
void *delend(struct node *head,int n);
void *square(struct node *head);
void *merge(struct node *head,int n);
struct node *circular(struct node *head);
int count(struct node *head);
main()
{
	head=(struct node *)malloc(sizeof(struct node *));
	head=create_list(head,5);
	head=circular(head);
	display(head);
}
struct node *create_list(struct node *head,int n)
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
void display(struct node *head)
{
	printf("\n");
	struct node *temp=head;
	while(temp!=NULL)
	{
		printf("%d-",temp->data);
		temp=temp->next;
	}
}
void *addbegin(struct node *head)
{
	int i;
	struct node *k=(struct node *)malloc(sizeof(struct node *));
	printf("\nEnter your element to be inserted:");
	scanf("%d",&k->data);
	k->next=head;
	head=k;
	return head;
}
void *addmiddle(struct node *head)
{
	struct node *temp=head;
	struct node *prev;
	struct node *new_node=(struct node *)malloc(sizeof(struct node *));
	int loc;
	int i=1;
	printf("Where do you want to enter the node:");
	scanf("%d",&loc);
	printf("Enter the data:");
	scanf("%d",&new_node->data);
	while(i<loc)
	{
		prev=temp;
		temp=temp->next;
		i++;
	}
	prev->next=new_node;
	new_node->next=temp;
	return head;
}
void *addend(struct node *head,int n)
{
	struct node *n1=head;
	int i;
	while(i<n)
	{
		n1=n1->next;
		i++;
	}
	struct node *k=(struct node *)malloc(sizeof(struct node *));
	printf("\nEnter your element to be inserted");
	scanf("%d",&k->data);
	n1->next=k;
	k->next=NULL;
return head;
}
void *delbegin(struct node *head)
{
	head=head->next;
	return head;
}
void *delend(struct node*head,int n)
{
	int i=1;
	struct node *temp=head;
	struct node *prev;
	while(i<n)
	{
		prev=temp;
		temp=temp->next;
		i++;
	}
	prev->next=NULL;
	return head;
}
void *square(struct node *head)
{
	struct node *n1=head;
	while(n1!=NULL)
	{
	n1->data=n1->data*n1->data;
	n1=n1->next;
	}
	return head;
}
void *merge(struct node *head,int n)
{
	int n1;
	int i=1;
	struct node *k=head;
	struct node *head1=(struct node *)malloc(sizeof(struct node));
	head1=create_list(head1,5);
	while(i<n)
	{
		k=k->next;
		i++;
	}
	k->next=head1;
	return head;
}
int count(struct node *head)
{
	int c=0;
	while(head!=NULL)
	{
		c++;
		head=head->next;
	}
	printf("\n %d",c);
}
struct node *circular(struct node *head)
{
	struct node *h1=head;
	while(h1->next)
	h1=h1->next;
	h1->next=head;
	return head;
}
