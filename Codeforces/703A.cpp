#include<bits/stdc++.h>
using namespace std;
int main()
{
	vector<int>v;
	int n,k;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>k;
		v.push_back(k);
	}
	sort(v.rbegin(),v.rend());
	for(i=1;i<n;i++)
		sum+=v[i]-v[0];
	cout<<sum;
}
