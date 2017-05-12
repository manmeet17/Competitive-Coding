#include<stdio.h>
#include<stdlib.h>
struct tree
{
	int info;
	struct tree *left;
	struct tree *right;
};
typedef struct tree *bstnode;
bstnode insert(bstnode t,int x);
bstnode del(bstnode t,int x);
void inorder(bstnode t);
void postorder(bstnode t);
void preorder(bstnode t);
main()
{
	bstnode t=NULL;
	t=insert(t,10);
	t=insert(t,20);
	t=insert(t,5);
	t=insert(t,8);
	inorder(t);
	printf("\n");
	preorder(t);
	printf("\n");
	postorder(t);
}
bstnode insert(bstnode t,int x)
{
	if(t==NULL)
	{
		t=(bstnode)malloc(sizeof(struct tree));
		t->info=x;
		t->left=t->right=NULL;
	}
	else
	{
		if(x<t->info)
		t->left=insert(t->left,x);
		else if(x>t->info)
		t->right=insert(t->right,x);
	}
	return t;
}
bstnode del(bstnode t,int x)
{
	bstnode temp;
	if(t==NULL)
		printf("Not Found");
	else if(x<t->info)
		t->left=del(t->left,x);
	else if(x>t->info)
		t->right=del(t->right,x);
	else
	{
		if(t->left && t->right)
		{
			temp=FindMin(t->right);
			t->info=temp->info;
			t->right=del(t->right,temp->info);
		}
		else
		{
			temp=t;
			if(t->left==NULL)
				t=t->right;
			else if(t->right=NULL)
				t=t->left;
			free(temp);
		}
	}
	return t;
}
/*
 This part of the program is just to display the tree, the left subtree first and then the right subtree.
 
 
display(bstnode t)
{
	bstnode temp=t;
	if(temp->left)
	{
		printf("%d\n",temp->info);
		display(temp->left);
	}
	else if(temp->right)
	{
		printf("%d\n",temp->info);
		display(temp->right);
	}
	else
	{
	printf("%d\n",temp->info);
	}
}
displayright(bstnode t)
{
		bstnode temp=t;
	if(temp->right)
	{
		printf("%d\n",temp->info);
		display(temp->right);
	}
	else if(temp->left)
	{
		printf("%d\n",temp->info);
		display(temp->left);
	}
	else
	{
	printf("%d\n",temp->info);
	}
	
}
*/
void inorder(bstnode t)
{
	if(t==NULL)
	return;
	inorder(t->left);
	printf("%d ",t->info);
	inorder(t->right);
}
void postorder(bstnode t)
{
	if(t==NULL)
	return;
	postorder(t->left);
	postorder(t->right);
	printf("%d ",t->info);
}
void preorder(bstnode t)
{
	if(t==NULL)
	return;
	printf("%d ",t->info);
	preorder(t->left);
	preorder(t->right);
}
