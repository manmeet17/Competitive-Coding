#include<iostream>
using namespace std;
const int N = 1e5 + 10;
int n,q;
int t[2*N];
void update(int x,int y){
for(t[x+=n]=y; x>1;x>>=1){
t[x>>1] = min(t[x],t[x^1]);
}
}
int query(int l, int r){
int res = 1e8;
for(l+=n,r+=n;l<r;l>>=1,r>>=1){
if(l&1) res = min(res,t[l++]);
if(r&1) res = min(t[--r],res);
}
return res;
}
int main(){
ios_base::sync_with_stdio(false);
cin.tie(NULL); cout.tie(NULL);
cin>>n>>q;
for(int i=0;i<n;i++){
cin>>t[i+n];
}
for(int i=n-1;i>0;i--){
t[i] = min(t[i<<1],t[i<<1|1]);
}
char qt;
int l,r;
while(q--){
cin>>qt;
if(qt=='q'){
cin>>l>>r;
cout << query(l-1,r) <<"\n";
}else{
cin>>l>>r;
update(l-1,r);
}
}
return 0;
}