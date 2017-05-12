#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<n;i++)
using namespace std;
int main()
{
	int n,d,x,s=0,c=0;
	cin>>n>>d;
	rep(i,n)
	{
		cin>>x;
		s+=x;
		if(i!=n-1)
		{
		    s+=10;
		    c+=2;
		}
	}
	if(s>d)
	cout<<"-1";
	else
	cout<<c+(d-s)/5;
}
