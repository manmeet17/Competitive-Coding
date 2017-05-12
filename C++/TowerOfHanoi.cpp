#include <iostream>
using namespace std;
void hanoi(int n,int from,int to,int aux)
{
	if(n==1)
	{
	cout<<"Moving Disk 1 from "<<from<<" to "<<to<<endl;
	return;
	}
	hanoi(n-1,from,aux,to);
	cout<<"Moving disk "<<n<<" from "<<from<<" to "<<to<<endl;
	hanoi(n-1,aux,to,from);
}
int main()
{
	
	hanoi(4,1,3,2);
}
