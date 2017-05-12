#include <iostream>
#include<vector>
using namespace std;

int main()
{
    int n,m,a,b;
    cin>>n>>m;
    int mat[n][n];
    for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
    {
        mat[i][j]=0;
    }
    for(int i=0;i<m;i++)
    {
        cin>>a>>b;
        mat[a][b]=1;
    }
    int q;
    cin>>q;
    for(int i=0;i<q;i++)
    {
        cin>>a>>b;
        if(mat[a][b]==0)
        cout<<"NO"<<endl;
        else
        cout<<"YES"<<endl;
    }
    return 0;
}

