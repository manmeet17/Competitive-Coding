#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int t;
        cin>>t;
        while(t--){
        int n,x;
        cin>>n;
        vector<int>nums;
        for(int i=0;i<n;i++){
            cin>>x;
            nums.push_back(x);   
        }
	int len=nums.size();
        vector <int> adj[len+1];
        bool vis[len];
        int lvl[len];
        
        for(int i=0;i<len;i++)
            vis[i]=false;
        
        for(int i=0;i<len-1;i++){
            if(nums[i]>0){
                for(int j=i+1;j<=nums[i]+i;j++){
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                    if(j==len-1)
                        break;
                }
            }
        }
        
        queue<int>q;
        q.push(0);
        lvl[0]=0;
        vis[0]=true;
        while(!q.empty()){
            int p=q.front();
            q.pop();
            for(int i=0;i<adj[p].size();i++){
                if(vis[adj[p][i]]==false){
                    q.push(adj[p][i]);
                    vis[adj[p][i]]=true;
                    lvl[adj[p][i]]=lvl[p]+1;
                }
            }
        }
        
        if(vis[len-1]==true)
            cout<<lvl[len-1]<<endl;
        else
            cout<<-1<<endl;

        }

}
