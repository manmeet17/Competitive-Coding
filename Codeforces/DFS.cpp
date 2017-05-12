#include<iostream>
#include<vector>
#include<stack>
using namespace std;
int main()
{
	int n, m, a, b;
	cin >> n >> m;
	vector<long long int>v[10005];
	for (int i = 0;i < m;i++)
	{
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	int x,c=0;
	vector<bool>vis;
	cin >> x;
	vis[x] = true;
	stack<int>s;
	s.push(x);
	cout<<s.top()<<endl;
	while (!s.empty())
	{
		int top = s.top();
		s.pop();
		if (top == x)
			c++;
		if (c == 2)
			break;
		for (int j = 0;j < v[top].size();j++)
		{
			if (vis[j] == false) {
				s.push(vis[j]);
				vis[j] = true;
			}
		}
	}
	c = 0;
	for (int i = 0;i < vis.size();i++)
	{
		if (vis[i] == false)
			c++;
	}
	cout << c << endl;
}
