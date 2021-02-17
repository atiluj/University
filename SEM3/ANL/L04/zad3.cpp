#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

double wypisz(double q, double r){
    double wynik1, wynik2;
    double x = pow(r+sqrt(q*q*q+r*r),(1.0/3.0));

    wynik1 = x+pow(r-sqrt(q*q*q + r*r),(1.0/3.0));
    wynik2 = (2*r)/(x*x + (1.0/x)*(1.0/x)*q*q + q);
    
    cout<<setprecision(12)<<wynik1<<endl;
    cout<<setprecision(12)<<wynik2<<endl;
    cout<<endl<<pow(wynik1, 3)+3*q*wynik1-2*r<<endl;
    cout<<endl<<pow(wynik2, 3)+3*q*wynik2-2*r<<endl;
    cout<<"----------------------"<<endl;
}

int main(){
    double r, q;

    for(int i=0; i<100; i++){
        cout<<"r:  ";
        cin>>r;
        cout<<endl;
        cout<<"q:  ";
        cin>>q;
        cout<<endl;

        wypisz(q, r);
    }



    return 0;
}
