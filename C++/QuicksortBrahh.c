#include <stdio.h>
#include <string.h>
main()
{
	int i;
	char a[8][10]= {"man","damn","corn","fork","jiff","hay","silly","phem"};
	quicksort(a,0,7);
	for (i=0;i<8;i++)
	{
		printf("%s\t",a[i]);
	}
}
void quicksort(char a[][10],int p,int r)
{
	int q;
	if (p<r)
	{
		q=partition(a,p,r);
		quicksort(a,p,q);
		quicksort(a,q+1,r);
	}
}
int partition(char a[][10],int p,int r)
{
	int i,j;
	char x[10],temp[10];
	strcpy(x,a[p+(r-p)/2]);
	i=p-1;
	j=r+1;
	while(1)
	{
		do
		{
			j=j-1;
		}while (strcmp(a[j],x)>0);
		do
		{
			i=i+1;
		}while (strcmp(a[i],x)<0);
		if (i<j)
		{
			strcpy(temp,a[i]);
			strcpy(a[i],a[j]);
			strcpy(a[j],temp);
		}
		else
			return j;
	}
}

