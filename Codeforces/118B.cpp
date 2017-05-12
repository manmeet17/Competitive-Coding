#include<iostream>
using namespace std;
int main()
{
	int n;
	cin>>n;
	int arr[2*n+1][2*n+1];
	for(int i=0;i<2*n+1;i++)
	{
		int val=0;
		for(int j=0;j<2*n-i;j++)
		{
			cout<<"\t";
		}
		cout<<endl;
		for(int k=0;k<i+1;k++)
		{
			cout<<k<<" ";
		}
	}
}
