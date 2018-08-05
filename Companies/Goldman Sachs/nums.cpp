#include<bits/stdc++.h>
using namespace std;
int main()
 {
	//code
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int arr[n];
	    int k=0,x;
	    for(int i=0;i<n;i++)
	    {
	        cin>>x;
	        int num=x;
	        while(num!=0)
	        {
	            int no = num%10;
	            if(no>=1&&no<=3)
	            {
	                num/=10;
	            }
	            else
	             break;
	        }
	        if(num==0)
	        arr[k++]=x;
	    }
	    sort(arr,arr+k);
	    for(int i=0;i<k;i++)
	    cout<<arr[i]<<" ";
	    if(k==0)
	    cout<<"-1";
	    cout<<endl;
	}
	return 0;
}
