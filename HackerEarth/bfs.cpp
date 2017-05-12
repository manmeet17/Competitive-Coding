#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,n,a,b,x;
	cin >> t;
	for (int i = 0;i < t;i++)
	{
		cin >> n;
		vector< pair<int,int> >v[n];
		for (int j = 0;j < n-1;j++)
		{
			cin >> a>>b>>x;
			v[a].push_back(make_pair(b,x));
			v[b].push_back(make_pair(a, x));
		}

	}
}