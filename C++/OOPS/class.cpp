#include<bits/stdc++.h>
using namespace std;

class Geeks
{
    private:
        double rad;
    public:
        string geekname;
        void printname();
        void print()
        {
            cout<<"Geek: "<<geekname<<endl;
        }

        double compute(double r)
        {
            rad=r;
            double area=3.14*r*r;
            cout<<"Area: "<<area<<endl;
        }

        Geeks()
        {
            rad=0;
            cout<<"Default Constructor called"<<endl;
            cout<<rad<<endl;
        }

        Geeks(double r)
        {
            rad=r;
            cout<<"Constructor called"<<endl;
            cout<<rad<<endl;
        }
};

void Geeks::printname()
{
    cout<<"Geeky fellow is: "<<geekname<<" Radius: "<<rad<<endl;
}

int main()
{
    Geeks obj(20);
    obj.geekname="Manmeet";
    obj.print();
    // obj.compute(100);
    obj.printname();
    return 0;
}
