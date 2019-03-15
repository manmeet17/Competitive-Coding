#include <iostream>
#include <algorithm>
#include <bitset>
#include <stdio.h>
#include <set>
#include <string>
#include <cstring>
#include <queue>
using namespace std;


void func(int l,int r, int di[]){
	if(l==r)return;
	int mid=(r+l)/2;
	int len=(r-l+1)/2;
	func(l,mid,di);
	func(mid+1,r,di);
	for(int i=l;i<=mid;i++){
		di[i]+=di[i+len];
	}
}
int main(){
	int t;
	cin>>t;
	while(t--){
    int n;
    long int arr[3000000];
    char str[666];
    int di[(1<<5)+10];
	scanf("%d",&n);
	int cntt=0;
	for(int i=0;i<n;i++){
		scanf("%s",str);
		arr[i]=0;
		int k=strlen(str);
		for(int j=0;j<k;j++){
			arr[i]|= 1<<(str[j]-'a');
		}
		if(arr[i]==(1<<5)-1){
			cntt++;
		}
		di[arr[i]]++;
	}
	func(0,(1<<4)-1,di);
	long long sol=0;
	for(int i=0;i<n;i++){
		sol+=di[(1<<5)-1 -arr[i]];
	}
	sol-=cntt;
	sol/=2;
	sol+=cntt;
	printf("%lld\n",sol);
}
}