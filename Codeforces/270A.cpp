#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	int t;
	cin>>t;
	float a;
	for(int i=0;i<t;i++)
	{
		cin>>a;
		float n=360/(180-a);
		if(floor(n)==n && n>=3)
		cout<<"YES"<<endl;
		else
		cout<<"NO"<<endl;
	}
}
