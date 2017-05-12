#include<stdio.h>
int left(int i)
{
	return 2*i+1;
}
int right(int i)
{
	return 2*i+2;
}
void heapify(int a[],int i,int n)
{
	int l,r,large,temp;
	l=left(i);
	r=right(i);
	if((l<=n-1) && (a[l]>a[i]))
	large=l;
	else
	large=i;
	if((r<=n-1) &&(a[r]>a[large]))
	large=r;
	if(large!=i)
	{
		temp=a[i];
		a[i]=a[i+1];
		a[i+1]=temp;
		heapify(a,large,n);
	}
}
void buildHeap(int a[],int n)
{
	int i;
	for(i=(n-1)/2;i>=0;i--)
	{
		heapify(a,i,n);
	}
}
void Heapsort(int a[],int n)
{
	int i,m,temp;
	buildHeap(a,n);
	m=n;
	for(i=n-1;i>=1;i--)
	{
		temp=a[0];
		a[0]=a[i];
		a[i]=temp;
		m=m-1;
		Heapify(a,0,m);
	}
}
main()
{
	int i;
	int a[5]={24,18,36,5,84};
	Heapsort(a,5);
	for(i=0;i<5;i++)
	{
		printf("%d\n",a[i]);
	}
}
