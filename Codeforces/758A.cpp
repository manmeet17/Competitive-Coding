#include<bits/stdc++.h>
using namespace std;
int main()
{
	vector<int>v;
	int n,k,sum=0;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>k;
		v.push_back(k);
	}
	sort(v.rbegin(),v.rend());
	for(int i=1;i<n;i++)
		sum+=v[0]-v[i];
	cout<<sum;
}
