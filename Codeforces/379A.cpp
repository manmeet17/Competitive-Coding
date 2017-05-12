#include<iostream>
using namespace std;
int main()
{
	int a,b;
	cin>>a>>b;
	int t=a;
	while(a>=b)
	{
		t+=a/b;
		a=a/b+a%b;
	}
	cout<<t<<endl;
}
