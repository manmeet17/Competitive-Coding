#include<iostream>
#include<string>
using namespace std;
int main()
{
	int n,m;
	string c;
	bool d=false;
	cin>>n>>m;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			cin>>c;
			if(c!="W" && c!="B" && c!="G")
			{
				cout<<"#Color"<<endl;
				d=true;
				break;
			}
		}
		if(d==true)
		break;
	}
	if(d==false)
	cout<<"#Black&White";
}
