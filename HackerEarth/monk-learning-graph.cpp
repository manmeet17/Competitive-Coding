#include<iostream>
#include <vector>
#include<algorithm>
#define rep(i,n,t) for(int i=t;i<=n;i++)
using namespace std;
    int main()
    {
        int x, y, n, e,k;
        cin>>n>>e>>k;
        vector<int> v[n];
        vector<int> val;
        rep(i,n-1,0)
		{
        	cin>>x;
        	val.push_back(x);
		}
		rep(i,e,1){
			cin>>x>>y;
			v[x-1].push_back(val[y-1]);
		}
		rep(i,n,1)
		{
			sort(v[i-1].rbegin(),v[i-1].rend());
			cout<<v[i-1][k-1];
		}
    return 0;
    }
