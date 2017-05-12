#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    set<char>st;
    getline(cin, s);
    for(int i=0, j=s.size(); i!=j; ++i)
    {
        if(s[i]!=' '&&s[i] != ',' && s[i]!='{' && s[i] != '}') st.insert(s[i]);
    }
    cout << st.size() << endl;

}
