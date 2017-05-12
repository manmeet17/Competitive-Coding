#include<iostream>
#include<string>
using namespace std;
main()
{
	int id1,id2,tempc,tempf;
	string us,india;
	cin>>id1>>us>>tempf>>id2>>india>>tempc;
	float c=(tempf-32)*(5.0/9.0);
	if(tempf>c)
	cout<<"greater";
	else
	cout<<"lesser";
}
