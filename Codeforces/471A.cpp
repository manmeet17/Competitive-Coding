#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int k,item;
	vector<int>v;
	bool f=false;
	for(int i=0;i<6;i++)
	{
	cin>>k;
	v.push_back(k);
	}
	vector<int>::iterator it;
	for(it=v.begin();it!=v.end();it++)
	{
		if(count(v.begin(),v.end(),*it)==4)
		{
		item=*it;
		f=true;
		break;
		}
	}
	if(f==false)
	cout<<"Alien";
	int i=0;
	int a[2];
	for(it=v.begin();it!=v.end();it++)
	{
		if(*it!=item)
		{
		a[i]=*it;
		i++;
	}
	}
if(a[0]!=a[1])
cout<<"Elephant"<<endl;
else
cout<<"Bear";
}
