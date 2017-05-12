#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int n, t, x,f=0;
	cin >> n >> t;
	vector<int>v;
	for (int i = 0;i < n;i++)
	{
		cin >> x;
		v.push_back(x);
	}
	int ans = 1,j=1;
	while (j<=n)
	{
		ans += v[j-1];
		j = ans;
		if (ans == t) {
			cout << "YES";
			f = 1;
			break;
		}
	}
	if (f == 0)
		cout << "NO";
}
