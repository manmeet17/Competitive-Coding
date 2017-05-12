#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct edgelist;
typedef struct nodelist
{
	char city[10];
	struct nodelist *next;
	struct edgelist *adj;
	int out,in;
}Node;
typedef struct edgelist
{
	struct nodelist *dest;
	struct edgelist *link;
	int weight;
}Edge;
void BuildNodeList(Node *start)
{
	Node *curr, *prev=NULL;
	int i;
	int n;
	char c[10];
	printf("Enter no of nodes:");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		curr=(Node *)malloc(sizeof(Node));
		printf("Enter name of the city:");
		gets(c);
		strcpy(curr->city,c);
		curr->next=NULL;
		curr->adj=NULL;
		if(prev=NULL)
		start=curr;
		else
		prev->next=curr;
		prev=curr;
	}
}
void insertEdge(Node *start)
{
	Edge *curr,*prev;
	Node *temp,*ptr;
	int i,j,m,p,k;
	temp=start;
	for(i=1;i<=5;i++)
	{
		printf("Enter the number of adjacent nodes of %d",i);
		scanf("%d",&m);
		prev=NULL;
		for(j=1;j<=m;j++)
		{
			printf("Enter %d adjacent node of %d",j,i);
			scanf("%d",&k);
			curr=(Edge *)malloc(sizeof(Edge));
			printf("Enter weight of the edge:");
			scanf("%d",&curr->weight);
			ptr=start;
			curr->link=NULL;
			p=1;
			while(p<k)
			{
				ptr=ptr->next;
				p++;
			}
			curr->dest=ptr;
			if(prev=NULL)
				temp->adj=curr;
			else
				prev->link=curr;
			prev=curr;
		}
	}
}
void outdegree(Node *start)
{
	Node *temp=start;
	Edge *curr;
	while(temp!=NULL)
	{
	curr=temp->adj;
	while(curr!=NULL)
	{
		temp->out++;
		curr=curr->link;
	}
	printf("Outdegree of vertex %s is:%d",temp->city,temp->out);
	temp=temp->next;
	}
}
void indegree(Node *start)
{
	Node *temp=start,*ptr;
	Edge *curr;
	while(temp!=NULL)
	{
		curr=temp->adj;
		while(curr!=NULL)
		{
			ptr=curr->dest;
			ptr->in++;
		}
		printf("Indegree of vertex %s is:%d",temp->city,temp->in);
		temp=temp->next;
	}
}
void display(Node *start)
{
	Node *nptr;
	Edge *eptr;
	nptr=start;
	while(nptr!=NULL)
	{
		eptr=nptr->adj;
		printf("%d",nptr->city);
		while(eptr!=NULL)
		{
			printf("%d",eptr->dest->city);
			eptr=eptr->link;
		}
		nptr=nptr->next;
	}
}
main()
{
	Node *start;
	BuildNodeList(start);
	insertEdge(start);
	display(start);
	indegree(start);
	outdegree(start);
}
