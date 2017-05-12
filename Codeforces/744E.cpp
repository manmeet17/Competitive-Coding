#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<math.h>
#include<cassert>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<map>
#include<ctime>
#include<queue>
#include<stack>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<bitset>
#include<valarray>
#include<iterator>
#include<list>
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define S second
#define ld long double
#define F first
#define y1 LOL
#define ld long double
#define pb push_back
#define len length
#define sz size
#define beg begin
const ll INF = (ll)1e18 + 123;
const int inf=(int)2e9 + 123; 
const int mod=1e9+7;
using namespace std;
int n, m, t[500011][21][2], a[100011], add[100011];
void build(int v = 1, int tl = 1, int tr = n){
	if(tl == tr){
		int x = a[tl];
		for(int i = 19; i >= 0; i --){
			if(x >= (1 << i)){
				x -= (1 << i);
				t[v][i][1] ++;
			}else
				t[v][i][0] ++;
		}
		return;
	}
	int mid = (tl + tr) / 2;
	build(v * 2, tl, mid);
	build(v * 2 + 1, mid + 1, tr);
	for(int i = 19; i >= 0; i --){
		t[v][i][1] = t[v * 2][i][1] + t[v * 2 + 1][i][1];
		t[v][i][0] = t[v * 2][i][0] + t[v * 2 + 1][i][0];
	}
	
}
void push(int v, int tl, int tr){
	if(!add[v])
		return;
	int x = add[v];
	for(int i = 19; i >= 0; i --){
		if(x >= (1 << i)){
			swap(t[v][i][0], t[v][i][1]);
			x -= (1 << i);
		}
	}
	if(tl != tr){
		add[v * 2] = add[v * 2] ^ add[v];
		add[v * 2 + 1] = add[v * 2 + 1] ^ add[v];
		add[v * 2 + 2] = add[v * 2 + 1] ^ add[v]
	}
	add[v] = 0;
}
void upd(int l, int r, int x, int v = 1, int tl = 1, int tr = n){
	push(v, tl, tr);
	if(tl >= l && tr <= r){
		add[v] = add[v] ^ x;
		push(sv, tl, tr);
		return;
	}
	if(tl > r || tr < l)
		return;
	int mid = (tl + tr) / 2;
	upd(l, r, x, v * 2, tl, mid);
	upd(l, r, x, v * 2 + 1, mid + 1, tr);
	for(int i = 19; i >= 0; i --){
		t[v][i][0] = t[v * 2][i][0] + t[v * 2 + 1][i][0];
		t[v][i][1] = t[v * 2][i][1] + t[v * 2 + 1][i][1];
	}
}
ll get(int l, int r, int v = 1, int tl = 1, int tr = n){
	push(v, tl, tr);
	if(tl > r || tr < l)
		return 0;
	if(tl >= l && tr <= r)
	{
		ll ans = 0;
		for(int i = 19; i >= 0; i --)
		{
			ll x = (1 << i);
			ans += x * t[v][i][1];
		}
		return ans;
	}
	int mid = (tl + tr) / 2;
	ll ans = get(l, r, v * 2, tl, mid) + get(l, r, v * 2 + 1, mid + 1, tr);
	for(int i = 19; i >= 0; i --){
		t[v][i][0] = t[v * 2][i][0] + t[v * 2 + 1][i][0];
		t[v][i][1] = t[v * 2][i][1] + t[v * 2 + 1][i][1];
	}
	return ans;
}
int main(){
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		scanf("%d", &a[i]);
	build();
	scanf("%d", &m);
	for(int i = 1; i <= m; i ++){
		int l, r, type, x;
		scanf("%d%d%d", &type, &l, &r);
		if(type == 1){
			printf("%I64d\n", get(l, r));
		}else{
			scanf("%d", &x);
			upd(l, r, x);
		}
	}
	return 0;
}
