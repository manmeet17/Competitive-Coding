#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long n,k,i,c=0;
	cin>>n>>k;
	for(i=1;i<=n;i++)
	{
		if(n%i==0)
		c++;
		if(c==k)
		break;
	}
	if(c<k)
	cout<<-1;
	else
	cout<<i;
}
