#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct trie_node
{
	char data;
	struct trie_node *child[26];
}tn;
tn *newnode(char x)
{
	int i;
	tn *n;
	n=(tn *)malloc(sizeof(tn));
	n->data=x;
		for (i=0;i<26;i++)
			n->child[i]=NULL;
	return n;
}/*
t *create_trie(struct trie_node *root_trie)
{
	int i;
	t *root=(t *)malloc(sizeof(t));
	root->next=newnode();
	return root;
}*/
void insert(struct trie_node * root,char x[])
{
	/*if (root_trie==NULL)
	{
		printf("\nNULL trie\n");
		return;
	}
	int index,l,length=strlen(x);
	struct trie_node *temp;
	temp=root_trie->root_node;
	for (l=0;l<=length;l++)
	{
		index=(int)x[l]-(int)'a';
		temp->data=x[l];
		if (!temp->child[index])
		{
			return;
		}
		temp=temp->child[index];
	}
	temp->data=root_trie->count;*/
	int index,l,length=strlen(x);
	tn *temp=root;
	for (l=0;l<=length;l++)
	{
		index=(int)x[l]-(int)'a';
		if(temp->child[index]==NULL)
		{
			temp->child[index]=newnode(x[l]);	
		}
			temp=temp->child[index];
	}
}
void main()
{
	int i;
	char a[][5]={"here","they","horse","pair"};
	tn *root=NULL;
	root=newnode('\0');
	for (i=0;i<sizeof(a);i++)
		insert(root,a[i]);
}
