#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int n,p,q,x;
	cin>>n;
	cin>>p;
	vector<bool>v(n,false);
	for(int i=0;i<p;i++)
	{
		cin>>x;
		v[x-1]=true;
	}
	cin>>q;
	for(int i=0;i<q;i++)
	{
		cin>>x;
		v[x-1]=true;
	}
	bool b=true;
	for(int i=0;i<v.size();i++)
	{
		if(v[i]==false)
		{
		cout<<"Oh, my keyboard!"<<endl;
		b=false;
		break;
		}
	}
	if(b==true)
	cout<<"I become the guy."<<endl;
}
