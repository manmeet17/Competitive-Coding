#include<iostream>
using namespace std;
int sorted(int a[],int n)
{
	if(n==1)
	return 1;
	if(a[n-1]>a[n-2])
		return sorted(a,n-1);
	else
		return 0;
}

int main()
{
	int a[7]={1,2,3,4,8,6,7};
	cout<<sorted(a,7);
}
