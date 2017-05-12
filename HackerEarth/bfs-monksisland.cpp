#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,m,a,b;
        cin>>n>>m;
        vector<int>v[n+1];
        int level[n+1];
        bool vis[n+1];
        for(int i=0;i<n+1;i++)
            vis[i]=false;
        for(int j=0;j<m;j++)
        {
            cin>>a>>b;
            v[a].push_back(b);
            v[b].push_back(a);
        }
        queue <int> q;
        q.push(1);
        level[1] = 0;
        vis[1] = true;
        while(!q.empty())
        {
            int p = q.front();
            q.pop();
            for(int i = 0;i < v[p].size() ; i++)
            {
                if(vis[v[p][i]] == false)
                {
                    level[ v[ p ][ i ] ] = level[ p ]+1;                 
                     q.push(v[ p ][ i ]);
                     vis[ v[ p ][ i ] ] = true;
      }
            }
        }
        cout<<level[n]<<endl;
    }
}

